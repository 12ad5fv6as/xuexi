import psutil

print(psutil.cpu_count(logical=True))
print(psutil.cpu_percent(interval=1.0))
