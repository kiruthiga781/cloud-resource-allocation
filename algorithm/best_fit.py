def run(tasks, vms):
    total_wait = 0
    completed = 0
    for task in tasks:
        suitable_vms = [vm for vm in vms if vm["capacity"] >= task["time"]]
        if not suitable_vms:
            continue
        vm = min(suitable_vms, key=lambda x: x["capacity"])
        total_wait += task["time"] / vm["capacity"]
        completed += 1
    completion_rate = (completed / len(tasks)) * 100
    return {
        "Average Waiting Time": round(total_wait / completed if completed else 0, 2),
        "Resource Utilization": f"{round((completed / (len(vms)*len(tasks))) * 100, 2)}%",
        "Completion Rate": f"{round(completion_rate, 2)}%"
    }
