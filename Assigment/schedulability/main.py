import numpy as np
 
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
 
periods = []
for i in range(len(tasks)):
    periods.append(tasks[i][2])
    
hyperperiod = periods[0]
for p in periods[1:]:
    hyperperiod = abs(hyperperiod * p) // np.gcd(hyperperiod, p)
 
print(f"  The hyperperiod is : {hyperperiod} ms")

#%% Check utilization critera

U = 0
for task in tasks:
    U += task[1] / task[2]

print(f"Processor utilization : U = {U}")

if U <= 1:
    print("U <= 1 : the task set is schedulable")
else:
    print("U > 1 : the task set is not schedulable")
    
#%% Check workload  criteria

RT = 0
for task in tasks:
    n_jobs = hyperperiod // task[2]
    RT += n_jobs * task[1]

print(f"Response Time is : RT = {RT} ms")
if RT <= hyperperiod:
    print(f"RT <= H : the task set is schedulable")
else:
    print(f"RT > H : the task set is not schedulable")