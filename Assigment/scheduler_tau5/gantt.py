
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#%%

Hyperperiod = 80  # ms

colors = {
    "tau1": "#4C72B0",
    "tau2": "#DD8452",
    "tau3": "#55A868",
    "tau4": "#C44E52",
    "tau5": "#8172B2",
    "tau6": "#937860",
    "tau7": "#DA8BC3"
}

task_names = ["tau1", "tau2", "tau3", "tau4", "tau5", "tau6", "tau7"]

#%% Generate one Gantt chart per strategy

for strategy in ["FCFS", "SJF", "LJF"]:

    schedule = []
    with open(f"schedule_{strategy}.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            schedule.append({
                "task" : row["task"],
                "arrival" : float(row["arrival"]),
                "start" : float(row["start"]),
                "end" : float(row["end"]),
                "deadline" : float(row["deadline"]),
                "wait" : float(row["wait"]),
                "deadline_missed" : row["deadline_missed"] == "True"
            })


    # Plot Gantt chart 
    fig, ax = plt.subplots(figsize=(14, 5))
    fig.suptitle(f"Gantt Chart — {strategy}", fontsize=13, fontweight="bold")

    for entry in schedule:
        y        = task_names.index(entry["task"])
        duration = entry["end"] - entry["start"]
        
        # If deadline was missed, color the bar red, otherwise use the task color
        if entry["deadline_missed"]:
            color = "red"
        else:
            color = colors[entry["task"]]

        # Draw job bar
        ax.broken_barh([(entry["start"], duration)], (y - 0.4, 0.8), facecolors=color, edgecolor="white", linewidth=0.5)

        # Mark deadline with a vertical dashed line
        ax.axvline(x=entry["deadline"], ymin=y / len(task_names), ymax=(y + 1) / len(task_names), color="black", linestyle="--", linewidth=0.8)

    ax.set_yticks(range(len(task_names)))
    ax.set_yticklabels(task_names)
    ax.set_xlabel("Time (ms)")
    ax.set_xlim(0, Hyperperiod)
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    # Legend
    patches = [mpatches.Patch(color=colors[t], label=t) for t in task_names]
    patches.append(mpatches.Patch(color="red", label="deadline missed"))
    ax.legend(handles=patches, loc="upper right", fontsize=8)

    plt.tight_layout()
    plt.savefig(f"gantt_{strategy}_tau5.png", dpi=150)
    plt.show()
    print(f"Gantt chart saved to gantt_{strategy}_tau5.png")