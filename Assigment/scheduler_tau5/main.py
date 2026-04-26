import csv

#%% Task set definition (name, WCET, period)
tasks = [
    ("tau1", 139e-6, 10),   # C1 = 139 ns = 0.000139 ms
    ("tau2", 3, 10),
    ("tau3", 2, 20),
    ("tau4", 2, 20),
    ("tau5", 2, 40),
    ("tau6", 2, 40),
    ("tau7", 3, 80),
]
 
Hyperperiod = 80  # ms

#%% Generate all jobs over the hyperperiod (name, arrival time, deadline, wcet)

jobs = []
for name, C, T in tasks:
    n_jobs = Hyperperiod // T          # number of times this task runs
    for i in range(n_jobs):
        arrival = i * T               # job released at n * period
        deadline = arrival + T         # deadline = arrival + period
        jobs.append({"name" : name, "arrival" : arrival, "deadline" : deadline, "wcet" : C})
 
#%% Run for different strategies such as : First Come First Served / Shortest Job First / Longest Job First
for strategy in ["FCFS", "SJF", "LJF"]:
 
    time = 0.0           # current time
    total_wait = 0.0           # total waiting time across all jobs
    total_idle = 0.0           # total idle time of the CPU
    missed = 0             # number of missed deadlines
    jobs_not_exec = jobs.copy()   # jobs not yet executed
 
    schedule = []  # list to save executed jobs info
    
    while len(jobs_not_exec) > 0:
 
        available = [] # list of jobs that have already arrived
        for j in jobs_not_exec:
            if j["arrival"] <= time:
                available.append(j)
 
        if len(available) == 0: # no job ready, CPU is idle until the next arrival
            next_arrival = jobs_not_exec[0]["arrival"] # Take as reference (first job in list)
            for j in jobs_not_exec: # search a job with the earliest arrival comapre to the reference
                if j["arrival"] < next_arrival:
                    next_arrival = j["arrival"]
                    
            total_idle += next_arrival - time
            time        = next_arrival
            continue # jump forward in time to the next available job
 

        # If other jobs than tau5 are available, remove tau5 from selection
        available_without_tau5 = []
        for j in available:
            if j["name"] != "tau5":
                available_without_tau5.append(j)
        
        if len(available_without_tau5) > 0:
            available = available_without_tau5  # tau5 is deprioritized

        selected = available[0] # Take as reference for the first available job 

        if strategy == "FCFS": # pick the job that arrived first
            for j in available: # search a job with the earliest arrival time compare to the reference
                if j["arrival"] < selected["arrival"]:
                    selected = j # update reference if earlier arrival found
 
        elif strategy == "SJF": # pick the job with smallest WCET
            for j in available: # search a job with the smallest WCET compare to the reference
                if j["wcet"] < selected["wcet"]: 
                    selected = j # update reference if smaller WCET found
 
        elif strategy == "LJF": # pick the job with largest WCET
            for j in available: # search a job with the longest WCET compare to the reference
                if j["wcet"] > selected["wcet"]:
                    selected = j # update reference if longer WCET found
 
        # Compute waiting time to know how long this job waited before starting
        total_wait += time - selected["arrival"] # If job came at time = 0s and it was executed at time 100s, it waited 100s
 
        # Execute the job
        time += selected["wcet"] # Time where it started to be execute + the worst case execution time
 
        # Check if deadline was missed
        if time > selected["deadline"]: # end time of the job exceeds deadline than we missed the deadline
            missed += 1
 
        
        schedule.append({
            "strategy" : strategy,
            "task" : selected["name"],
            "arrival" : selected["arrival"],
            "start" : time - selected["wcet"],  # start = end - wcet
            "end" : time,
            "deadline" : selected["deadline"],
            "wait" : time - selected["wcet"] - selected["arrival"],
            "deadline_missed" : time > selected["deadline"]
        })
 
    
        # Remove executed job from list of jobs not execute
        jobs_not_exec.remove(selected)
 
    # If CPU finishes before end of hyperperiod than we add the count remaining as idle
    if time < Hyperperiod:
        total_idle += Hyperperiod - time
 
    # Show the result for the strategy "x"
    print(f"Strategy : {strategy}")
    print(f"Total waiting time : {total_wait} ms")
    print(f"Total idle time : {total_idle} ms")
    print(f"Deadlines missed : {missed}")
    print(f"Verification of the result : Idle + Workload = {total_idle + 51.001112} ms (must be {Hyperperiod} ms)")
    print()
    
    with open(f"schedule_{strategy}.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["strategy", "task", "arrival", "start", "end", "deadline", "wait", "deadline_missed"])
        writer.writeheader()
        for row in schedule:
            writer.writerow(row)
    print(f"Saved to schedule_{strategy}.csv\n")