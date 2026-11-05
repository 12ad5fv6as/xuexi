import json

report = {"cpu_percent":25.5, "ok":True,"gpu":None}
text = json.dumps(report, ensure_ascii=False,allow_nan=False)
restored=json.loads(text)
print(text)
print(restored==report)
