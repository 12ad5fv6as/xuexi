## 第09章的目录与执行位置（必看）

当前 `lab/` 目录已经包含 `monitor/`、`tests/` 和 `student_examples/`。请在这一 README 所在目录执行测试，而不是 `chapter_code/`：

```bash
pwd
ls monitor tests student_examples
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python3 -m pytest -q student_examples/test_09_03_boundary.py
python3 -m pytest -q tests/test_rules.py
```

如果想亲自输入课件代码，请在此目录执行 `nano tests/test_09_03_practice.py`，保存后运行 `python3 -m pytest -q tests/test_09_03_practice.py`。不要覆盖已有 `tests/test_rules.py`。

---

# Week 1：Linux系统信息采集器（参考工程）

教学用途：读取CPU、内存、文件系统空间和高RSS进程，保存JSON，并验证失败行为。该程序不是生产监控平台，也不是AI模型。

## 环境和启动

Python 3.10+语法，优先在个人Linux或WSL Ubuntu环境学习。实测版本见上一级VALIDATION.txt。工作目录必须是这个README所在的lab目录。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m monitor --help
python -m monitor --interval 0.5 --top 5
python -m pytest -q
```

## 参数

`--interval`：大于0且不超过10的CPU采样秒数；`--top`：1到100的整数；`--cpu-threshold`：0~100有限数；`--disk-path`：查询所属文件系统的路径，默认/；`--output`：JSON路径；`--log-file`：日志路径。日志与报告不能指向同一路径。

默认输出为reports/system_report.json与logs/monitor.log。正常摘要在stdout，错误提示在stderr。状态0表示完成任务，1表示可预期运行失败，2通常表示argparse参数格式错误。

## 阅读源码顺序

rules.py → storage.py → collector.py → __main__.py，再按同名模块阅读tests。

正常采集会记录UTC起止时间、架构、逻辑CPU数、采样窗口、资源指标与进程列表。MiB按1024²、GiB按1024³字节计算。CPU阈值标签仅是课堂规则，不是硬件健康结论。

## 失败与不完整数据

单进程访问失败会跳过并计数；JSON中的incomplete=true表示检测到了这种不完整情况。false不保证完整宿主机可见性。整体读取、输出或日志初始化失败会返回非零状态。日志打不开时仍尝试通过stderr报告。

## 已知限制

顺序采样不是原子快照；未实现持续监控、GPU查询、网络诊断、原子写入、并发文件锁、日志轮转和断电恢复。序列化先于文件打开，可防止无效JSON对象先截断旧报告，但不能保证写入中断后完整。系统/容器可见范围可能不是物理主机全部资源。

测试用模拟对象检验逻辑，不能替代你的机器验证。不要公开未经脱敏的真实进程列表和日志。学习时先自己实现最小版本，再对照本工程。
