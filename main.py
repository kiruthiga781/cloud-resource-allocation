import json
from algorithms import round_robin, fcfs, priority, best_fit
from utils import generate_tasks, generate_vms

def run_simulation(tasks, vms):
    algorithms = {
        "Round Robin": round_robin.run,
        "FCFS": fcfs.run,
        "Priority": priority.run,
        "Best Fit": best_fit.run
    }

    results = []
    for name, func in algorithms.items():
        metrics = func(tasks, vms)
        results.append((name, metrics))
    return results

if _name_ == "_main_":
    try:
        with open("data/tasks.json") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = generate_tasks(10)

    vms = generate_vms(3)

    print("\n--- CLOUD RESOURCE ALLOCATION EFFICIENCY REPORT ---")
    results = run_simulation(tasks, vms)
    for name, metrics in results:
        print(f"\nAlgorithm: {name}")
        for k, v in metrics.items():
            print(f"{k}: {v}")
