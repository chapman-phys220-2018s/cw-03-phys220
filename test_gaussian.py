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
    """Tests known special cases of the interval. In this particular case, interval 0 to 1 with step size .2"""
    actual = [gaussian(0),gaussian(.2),gaussian(.4),gaussian(.6),gaussian(.8),gaussian(1)]
    trial = gaussian.interval(gaussian.g,0,1,.2)
    print("Testing interval 0 to 1:",actual," ?= ",trial)
    assert actual==trial

    trial = gaussian.interval(g(0), 1, 2, 0)
    print("Testing dx=0: ", actaul, " ?= ", trial)
    assert actual==trial

def test_integrate():
    """Checks the integration for correctness
    Test: integrate from 0 to 2 with spacing of steps at .5 (dx=.5)"""
    actual= 4.34441
    # This value was calculated with an online definite integral solver.
    trial= gaussian.integrate ([0,1,2],.5)
    print("This tests the interval from 0 to 2 with step size of .5: ",actual,"?=",trial)
    nose.tools.assert_almost_equal(actual, trial, 4)

def test_gauss_norm():
    """Checks for correct approximation when dx is small
    Test: interval from -5 to 5 with dx = .05"""
    actual= 44572.3
    # This value was calculated with an online definite integral solver.
    trial= gaussian.integrate(gaussian.g(-5,5,.05),.05)
    print("This tests the interval from -5 to 5 with small step size of .05: ",actual,"?=",trial)
    nose.tools.assert_almost_equal(actual, trial, 5)



