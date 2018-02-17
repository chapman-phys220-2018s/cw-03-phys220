#!/usr/bin/env python3

"""Gaussian Module Unit Tests"""

import nose
import math
import gaussian

def test_g():
    """Tests g with following trials:
        - g(0) ?= 1.0/sqrt(2pi)
    """
    # Pre-computed correct value of g(0)
    actual = 1.0/math.sqrt(2*math.pi)
    # Testing implementation
    trial = gaussian.g(0)
    # Debug messages like this are only printed if the test fails
    print("Testing g(0): ",actual," ?= ",trial)
    # an assert command is the actual test
    # for floats, be sure to use assert_almost_equal instead (here to 4 digits)
    nose.tools.assert_almost_equal(actual, trial, 4)

def test_interval():
    """Tests known special cases of the interval"""

def test_integrate():
    """Checks the integration for correctness"""

def test_gauss_norm():
    """Checks for correct approximation when dx is small"""

