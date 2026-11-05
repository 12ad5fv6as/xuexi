# 第09章逐节可运行示例

本目录随资料包自带，不需要你从零创建 `monitor/` 包。

运行前进入 `Week1_Learning_Kit_v4/lab/`，确认 `ls monitor tests student_examples` 可看到三个目录，并在当前目录创建虚拟环境、激活后安装 `requirements.txt`。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

```bash
python3 -m pytest -q student_examples/test_09_03_boundary.py
python3 -m pytest -q student_examples/test_09_04_parameters.py
python3 -m pytest -q student_examples/test_09_05_tmp_path.py
python3 -m pytest -q student_examples/test_09_06_monkeypatch.py
```

如果是独立输入练习代码，请在 `lab/` 目录下创建 `tests/test_09_03_practice.py` 等测试文件，切勿直接覆盖已有测试。
