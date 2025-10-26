def run(tasks, vms):
    total_wait = 0
    completed = 0
    i = 0
    for task in tasks:
        vm = vms[i % len(vms)]
        total_wait += task["time"] / vm["capacity"]
        completed += 1
        i += 1
    return {
        "Average Waiting Time": round(total_wait / len(tasks), 2),
        "Resource Utilization": f"{round((completed / (len(vms)*len(tasks))) * 100, 2)}%",
        "Completion Rate": "100%"
    }
