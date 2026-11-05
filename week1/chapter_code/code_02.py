metrics = {"cpu_percent": 25.5, "memory_percent": 60.0}
print(metrics["cpu_percent"])
print(metrics.get("gpu_percent"))   # None
for name, value in metrics.items():
    print(name, value)
