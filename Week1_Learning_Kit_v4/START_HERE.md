# 第09章测试目录在哪里？（先看这一页）

请先**解压完整 ZIP**，不要只单独下载 PDF/Word/HTML。两个目录确实放在压缩包内部的 `lab/` 中：

```text
Week1_Learning_Kit_v4/
  lab/
    monitor/
      __init__.py
      rules.py
      collector.py
      ...
    tests/
      test_rules.py
      test_collector.py
      test_storage.py
      test_cli.py
    student_examples/
      test_09_03_boundary.py
      test_09_04_parameters.py
      test_09_05_tmp_path.py
      test_09_06_monkeypatch.py
    requirements.txt
```

如果你目前在“解压得到的 `Week1_Learning_Kit_v4` 文件夹的上一级”目录，输入以下命令：

```bash
cd Week1_Learning_Kit_v4/lab
pwd
ls -ld monitor tests
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python3 -m pytest -q student_examples/test_09_03_boundary.py
python3 -m pytest -q tests/test_rules.py
```

如果已经进入 `lab/`，**不要再重复 `cd`**。如果 `ls` 提示目录不存在，请先执行 `pwd`、`ls` 并检查是否只下载了单独的 PDF 而没有解压 ZIP。不要在 `chapter_code/` 下运行第09章测试。

练习自己创建文件时，请先 `cd` 到 `lab/`，再输入 `nano tests/test_09_03_practice.py`。教程代码粘贴保存后用 `python3 -m pytest -q tests/test_09_03_practice.py` 执行。原有 `tests/test_rules.py` 不要覆盖。

---

# 第一周资料包：先创建文件夹，后保存代码

如果你要按照讲义手写 `chapter_code/03_01_basic_types.py`，请在 Ubuntu/WSL **普通命令行** 先执行：

```bash
mkdir -p ~/ai-systems-lab/week1-practice/chapter_code
cd ~/ai-systems-lab/week1-practice
nano chapter_code/03_01_basic_types.py
```

将代码写入后，按 `Ctrl+O`、回车、`Ctrl+X` 保存退出，再运行 `python3 chapter_code/03_01_basic_types.py`。

如果你打算直接运行压缩包里的参考源码，请先进入**解压得到的 `Week1_Learning_Kit_v4` 目录**；这个目录中已经有 `chapter_code/03_01_basic_types.py`，不必重新创建。先用 `pwd` 和 `ls chapter_code` 确认位置，再运行 `python3 chapter_code/03_01_basic_types.py`。

如果已在 nano 中看到“没有那个文件或目录”，最稳妥是先保存为当前目录中的 `03_01_basic_types.py`，退出后用 `mkdir -p chapter_code` 和 `mv 03_01_basic_types.py chapter_code/` 整理目录，不要直接丢弃已写代码。

---

# 第一周学习包：从这里开始

先打开 `Week1_Handbook.html` 或 `Week1_Handbook.pdf`，阅读第00章，不要从源码第一页开始。

阅读顺序：00导读 → 01环境 → 02Linux命令 → 03Python → 04JSON → 05模块与类 → 06异常日志 → 07进程与资源 → 08进阶机制 → 09测试 → 10Git → 11综合项目 → 12自测。附录A用于完成练习后对答案，附录B用于速查。

建议安排：Day1读00/01/02；Day2读03/04并写单文件采集器；Day3读05/06；Day4读07；Day5读08/09/10；Day6做11/12。全部用时约27小时是参考安排，不是个人学习速度保证。

## 文件用途

- `Week1_Handbook.pdf`：阅读和打印。
- `Week1_Handbook.html`：离线浏览、目录跳转、复制代码。
- `Week1_Handbook.docx`：批注与修改。
- `Week1_Handbook.md`：可编辑的Markdown原稿。
- `lab/`：完整参考工程与测试，从这个目录运行命令。
- `examples/`：独立短例子；运行位置决定相对输出路径。
- `exercises/`：分步练习与未完成函数，不是参考答案。
- `templates/`：环境、故障、周报模板。
- `VALIDATION.txt`：本次实际执行环境、测试和故障验证结果。

## 参考工程最小运行

进入lab，建立并激活虚拟环境，然后运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m monitor --interval 0.5 --top 5
```

Windows先打开WSL Ubuntu；不要在PowerShell直接执行source。不要使用sudo运行参考程序，不需要GPU。

参考工程测试通过不代表你已掌握。自己的目标是至少五项独立测试、五份故障记录和一个自己能解释的采集器。所有实验只在个人目录和授权环境进行。
