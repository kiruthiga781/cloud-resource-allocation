def run(tasks, vms):
    total_wait = 0
    completed = 0
    for i, task in enumerate(tasks):
        vm = vms[i % len(vms)]
        total_wait += (i * task["time"]) / vm["capacity"]
        completed += 1
    return {
        "Average Waiting Time": round(total_wait / len(tasks), 2),
        "Resource Utilization": f"{round((completed / (len(vms)*len(tasks))) * 100, 2)}%",
        "Completion Rate": "100%"
    }
