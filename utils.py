import random
import json
import os

def generate_tasks(n=10):
    tasks = [{"id": i, "time": random.randint(1, 10), "priority": random.randint(1, 5)} for i in range(n)]
    os.makedirs("data", exist_ok=True)
    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    return tasks

def generate_vms(n=3):
    return [{"id": i, "capacity": random.randint(5, 15)} for i in range(n)]
