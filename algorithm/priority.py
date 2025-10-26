def run(tasks, vms):
    tasks_sorted = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    total_wait = 0
    completed = 0
    for i, task in enumerate(tasks_sorted):
        vm = vms[i % len(vms)]
        total_wait += task["time"] / vm["capacity"]
        completed += 1
    return {
        "Average Waiting Time": round(total_wait / len(tasks_sorted), 2),
        "Resource Utilization": f"{round((completed / (len(vms)*len(tasks_sorted))) * 100, 2)}%",
        "Completion Rate": "100%"
    }
