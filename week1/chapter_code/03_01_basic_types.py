cpu_count = 8
cpu_percent = 25.5
system_name = "Linux"
is_healthy = True
last_error = None
samples = [10.0, 20.0, 30.0]
report = {"cpu_percent": cpu_percent,"system": system_name }

for name,value in [("cpu_count", cpu_count), ("cpu_percent", cpu_percent),
                   ("system_name", system_name), ("is_healthy", is_healthy),
                   ("last_error", last_error),("samples",samples),("report",report)]:
    print(name, "=", value, ";类型:", type(value).__name__)

print("是否没有报错信息：", last_error is None)
print("报告里的cpu使用率：", report["cpu_percent"])
