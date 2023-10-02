# cph23

Django Day CPH 2023

## Getting started

Make sure you have [poetry](https://python-poetry.org/) set up locally.

There are various ways to do this:

* Install poetry: https://python-poetry.org/docs/#installation
* Install poetry with [pyenv](https://github.com/pyenv/pyenv): https://python-poetry.org/docs/managing-environments/

What you do on your local is up to you. Just make sure to run below commands within the expected virtualenv. Pro tip: To avoid having to prefix every command with `poetry run`, enter a `poetry shell` first.

* Create and activate a Python virtual env. For example using pyenv:

 ```
 pyenv virtualenv 3.11 venv
 pyenv activate venv
 ```

* Install the required dependencies, including local `dev` dependencies (used for running tests):

 ```
 poetry install
 ```

Make sure you're in `project` directory before running the test commands.

* Run the tests

  ```
  $ cd project
  $ ./manage.py test
  ```

* Run tests and generate coverage report

  ```
  $ coverage run ./manage.py test && coverage report -m
  ```

`coverage` is configured its config file `.coveragerc`.

Sample output:

```
$ coverage run ./manage.py test && coverage report -m
Found 10 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.029s

OK
Destroying test database for alias 'default'...
Name                                      Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------------
config/__init__.py                            0      0      0      0   100%
config/settings.py                           18      0      0      0   100%
config/urls.py                                7      0      0      0   100%
orders/__init__.py                            0      0      0      0   100%
orders/apps.py                                4      0      0      0   100%
orders/migrations/0001_initial.py             6      0      0      0   100%
orders/migrations/0002_customer_code.py       4      0      0      0   100%
orders/migrations/__init__.py                 0      0      0      0   100%
orders/models.py                             31      1      4      0    97%   48
orders/serializers.py                        13      0      4      0   100%
orders/views.py                               9      0      0      0   100%
-------------------------------------------------------------------------------------
TOTAL                                        92      1      8      0    99%
```