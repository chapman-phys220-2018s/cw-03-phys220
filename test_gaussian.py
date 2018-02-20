#!/usr/bin/env python3

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#Devon Ball
#2313078
#dball@chapman.edu
#PHYS220 Spring 2018
#CW03 Exercise 1

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
    """Tests known special cases of the interval.
    In this particular case, interval 0 to 1 with step size .2 for f(x) = 2x"""

    def f(x):
        value = 2*x
        return value
    actual = [f(0),f(.2),f(.4),f(.6),f(.8),f(1)]
    trial = gaussian.interval(f,0,1,.2)

    print("Testing f(0):",actual[0]," ?= ",trial[0])
    nose.tools.assert_almost_equal(actual[0], trial[0], 4)

    print("Testing f(.2):",actual[1]," ?= ",trial[1])
    nose.tools.assert_almost_equal(actual[1], trial[1], 4)

    print("Testing f(.4):",actual[2]," ?= ",trial[2])
    nose.tools.assert_almost_equal(actual[2], trial[2], 4)

    print("Testing f(.6):",actual[3]," ?= ",trial[3])
    nose.tools.assert_almost_equal(actual[3], trial[3], 4)

    print("Testing interval f(.8):",actual[4]," ?= ",trial[4])
    nose.tools.assert_almost_equal(actual[4], trial[4], 4)

    print("Testing interval f(1.0):",actual[5]," ?= ",trial[5])
    nose.tools.assert_almost_equal(actual[5], trial[5], 4)

    len_actual = len(actual)
    len_trial = len(trial)
    print("Testing length of intervals:",len_actual," ?= ",len_trial)
    nose.tools.assert_almost_equal(len_actual, len_trial)

def test_integrate():
    """Checks the integration for correctness
    Test: integrate f(x) = 2x from 0 to 2 with spacing of steps at .000001 (dx=.000001)"""
    actual= 4
    def f(x):
        value = 2*x
        return value
    # This value was calculated with an online definite integral solver.
    i = gaussian.interval(f,0,2,.000001)
    trial= gaussian.integrate(i,.000001)
    print("This tests the integration of 2x from 0 to 2 with step size of .000001: ",actual,"?=",trial)
    nose.tools.assert_almost_equal(actual, trial, 3)

def test_gauss_norm():
    """Checks for correct integral of gaussian function when dx is small
    Test: interval from -5 to 5 with dx = .000001"""
    actual= .999999
    # This value was calculated with an online definite integral solver.
    trial= gaussian.integrate(gaussian.interval(gaussian.g,-5,5,.000001),.000001)

    print("This tests the interval from -5 to 5 with small step size of .000001: ",actual,"?=",trial)
    nose.tools.assert_almost_equal(actual, trial, 3)



