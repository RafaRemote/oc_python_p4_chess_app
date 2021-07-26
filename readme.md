# Project: Chess Tournament App

Menu

1. Usage
2. Technologies
3. Installation
4. Execution of the program
5. flake8 report

## 1 - Usage

Manage a chess tournament.  
App runs in the terminal.  
  
User creates a new tournament then  
User can enter players details and start the tournament.  
  
Rounds are automatically generated following the rules of pairing.  
  
User can access tables showing the status of the tournament at any time.  
Tables showing reports are printed in the terminal.  
  
Additional Feature: at any time user can change elo points of the players.  
  
### Tournament rules

**Pairing System**: Swiss  
**Number of Rounds**: 4  
**Number of Matches per Round**: 4  
**Number of Players**: 8  
**Points Assignment**: Classic  

- Winner: gets 1 points,  
- Loser: 0,  
- Draw: 0.5 each  

## 2 - Technologies

Programming language: Python 3.9.5  
Database engine: TinyDB.  

## 3 - Installation

You need to have Python installed on your machine.  
This script has been developed using python 3.9.5.  
Check your version of Python, if needed, upgrade your version.  
  
Open a terminal wherever you want then follow these steps:  

- Clone the repository:

```python
git clone https://github.com/RafaRemote/chess.git
```

- Move to the root folder:

```python
cd chess
```

- Install the virtual environment:

```python
python3 -m venv env
```

or on windows: py -m venv env

- Activate the virtual environment:

```python
source env/bin/activate
```

or on windows: env\Scripts\activate

- Upgrade pip:

```python
pip install --upgrade pip
```

- Install the project dependencies:

```python
pip install -r requirements.txt
```

## 4 - Execution of the program

From the terminal, be sure to be in the root folder (named 'chess'), then type:  

```python
python main.py
```

Now you just have to follow the menus which will be printed in the terminal.  

## 5 - flake8 report

In the root folder (named: 'chess') you'll find a folder called: 'flake8_rapport', including an index.html showing 'no flake8 violations'.  

To generate a new report:  

erase the folder 'flake8_rapport'.  
be sure to be in the root folder 'chess', then type:  

```python
flake8 --format=html --htmldir=flake8_rapport
```
