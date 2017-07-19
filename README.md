# Quadratic Equations Solver

pre-commit is bash script file which run several python unit-tests from tests.py 
before committing changes in the quadratic_equation.py code 

# Usage

Copy pre-commit file into ./.git/hooks/ directory of your project

# Sample output
```
.E..
======================================================================
ERROR: test_returns_none_for_complex_solution (__main__.QuadraticEquationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 23, in test_returns_none_for_complex_solution
    root1, root2 = get_roots(1, 2, 3)
  File "D:\Python\DevMan\14_pre_commit_hook\quadratic_equation.py", line 6, in get_roots
    root1 = (-b - sqrt(discriminant)) / (2 * a)
ValueError: math domain error

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (errors=1) unit tests failed, commit is not possible
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
