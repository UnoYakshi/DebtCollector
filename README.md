# DebtCollector

## Description
The main idea is to store all the debts between users, change it (add, subtract), and do it in a pretty web-service.

## Why?
1. We had problems in dormitory plenty of time(s) since no one remember how much who pays who two weeks later.
2. The reason for Py3 + Flask is that I needed to make a test task for one of the vacancy.

## Usage

### By-Hand
1. Activate virtualen '. venv/bin/activate'.
2. Install the dependencies (reqs.txt), I suggest using 'pip3 install reqs.txt'.
3. For the test reasons, just execute run.py with python3.
4. https://127.0.0.1/

P.S. Auto-setup will be added later.

### REST
1. /api/user/\<id\> -- retrieves user with the given id, or 404.
2. /api/user/\<login\> -- retrieves user with the given login, or 404.
3. /api/users -- retrieves all the users. TODO: flexiby.
