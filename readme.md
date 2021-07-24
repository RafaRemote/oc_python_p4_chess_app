# Project: Chess Tournament App

Menu

1. Installation
2. Excution of the program
3. flake8 report

## 1 - Installation

You need to have Python installed on your machine.
This script has been developed using python 3.9.5.
Check your version of Python, if needed, upgrade your version.

Open a terminal wherever you want then follow these steps:

```python
git clone https://github.com/RafaRemote/chess.git
```

```python
python3 -m venv env
```

```python
source env/bin/activate
```

```python
pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

## 2 - Execution of the program

From the terminal, be sure to be in the root folder. (named 'chess'), then type:

```python
python main.py
```

Now you just have to follow the menus which will be printed in the terminal.

## 3 - flake8 report

In the root folder (named: 'chess') you'll find a folder called: 'flake8_rapport', including an index.html showing 'no flake8 violations'.

To generate a new report:

erase the folder 'flake8_rapport'.
be sure to be in the root folder 'chess', then type:

```python
flake8 --format=html --htmldir=flake8_rapport
```
