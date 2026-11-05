import psutil

memory = psutil.virtual_memory()
print("total MiB:", memory.total / 1024**2)
print("available MiB:", memory.available / 1024**2)
print("percent:", memory.percent)
