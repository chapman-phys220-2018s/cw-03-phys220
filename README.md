# PHYS220 CW 3

**Author(s):** **Daniel, Devon, Myranda**

[![Build Status](https://travis-ci.org/chapman-phys220-2018s/cw-03-phys220.svg?branch=master)](https://travis-ci.org/chapman-phys220-2018s/cw-03-phys220)

## Specification

Complete the following exercises, placing your solutions into separate module files. (Use the module template in the info repository for guidelines on how to format such a module file.) In each file, do not write executable code directly, or use side effects like printing to the screen. Instead, write the solutions using callable functions that return values, so that you can write test functions in the indicated test files that demonstrate correct output using the nose framework. GitHub will automatically run your tests on every commit, indicating any failures via the Travis framework with build status above. Create a Jupyter notebook ```cw3.ipynb``` that imports each of your modules, discusses each of the problems, then demonstrates your working solution. Treat this notebook as a professional report. (See the template in the info repository for ideas on how to format your Jupyter notebook.)

1. Edit this README to update the Travis.ci link at the top. Done correctly, you should see a test status image in the README that indicates whether all your tests pass correctly. Look at the Travis.ci introduction page and complete steps 1 and 2: https://docs.travis-ci.com/user/getting-started/ - authorize it if necessary. Tests will then be rerun automatically after every git push to GitHub. (This is called "continuous code integration".) Once your repository is activated and the tests run, the image should turn green if all is well, or show an error if all is not well.

1. Exercise (```gaussian.py```, ```test_gaussian.py```)

  Idea: Consider a Gaussian function $$g(x) = \frac{1}{\sqrt{2\pi}}\,\exp\left[-\frac{x^2}{2}\right].$$ This is the "bell-curve" from statistics, centered at $x=0$ with standard deviation of $1$. Your task is to verify numerically that the integral of this function over $x$ is normalized to $1$.

  To accomplish this, complete the following subtasks:
  - Create a function `g(x)` in the code module `gaussian.py` that implements the Gaussian function for a particular argument `x`.

  - Create a function `interval(f, a, b, dx)` in the code module that takes four parameters: `f` is any function of a single variable, `a` and `b` are left and right endpoints of an interval $[a,b]$, and `dx` is the spacing between points in the interval. Have the function return a list of the form $$[f(a),f(a+dx),f(a+2dx),\cdots,f(a+(N-1)dx),f(b)],$$ where $N$ is the number of steps between $a$ and $b$ such that $b = a + N\,dx$.

  - Create a function `integrate(i, dx)` in the code module that takes two parameters: `i` is an interval as generated by the preceding function, and `dx` is the spacing of each step. Have this function return the integral of the interval. (Explain in your notebook how you chose to define this integral when explaining your work.)

  - Examine the test function `test_g` in the test module `test_gaussian.py` that uses `assert` to test a known value of `g` against your implementation. Check that this runs correctly when you run `python3 -m nose` from the terminal in your classwork repo. Try changing the test to be incorrect and try `python3 -m nose` again. Fix the test, and add one more correct assert line of your own.

  - Create a test function `test_interval` in the test module that checks known special cases of creating an interval.

  - Create a test function `test_integrate` in the test module that checks a simple integration example for correctness.

  - Create a test function `test_gauss_norm` that checks whether the integral of `g` correctly approximates unity when `dx` is a small parameter.  Show this result in your report notebook as well.

1. Ensure that your code and test modules are properly commented, and that you have correctly used docstrings to document your functions and module. Check that the python `help()` command correctly shows those docstrings in an interpreter. You should do this for all your python modules from now on.

1. Make sure you complete the Jupyter notebook, paying special care to format it well, and discuss the problem in full. Imagine that you will give this notebook to a colleague later for critique on both the content and the presentation of that content.

Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

- it's super convenient to have Travis checking for errors (MH)

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Myranda, Devon**
