#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

"""Consider the Gaussian function, defined as g(x), centered at x=0 with standard deviation of 1. Verify numerically that the integral of g(x) is normalized to 1."""

def g(x):
    """Gaussian function for given parameter: x"""
    value = (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)
    return value

def interval(f,a,b,dx):
    """Arguments    f- any function of a single variable
                    a- left end point on [a,b]
                    b- right end point in [a,b]
                    dx- spacing between coordinates"""
    k = 0
    inter = []
    while a+k*dx <= b:
        inter.append(f(a+k*dx))
        k+=1
    return inter

def integrate(i,dx):
    """Arguments    i- generated interval
                    dx- spacing between each step"""
    for k in range(n):
        integral = 0
        rect_area = i(k)*dx
        integral += rect_area
    return integral