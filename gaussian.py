#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


import math

"""Consider the Gaussian function, defined as g(x), centered at x=0 with standard deviation of 1.
Verify numerically that the integral of g(x) is normalized to 1.  This file contains three functions, a gaussian function,
a function that creates intervals, and a function that takes the integral of an interval"""

def g(x):
    """Gaussian function for given parameter: x"""
    value = (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)
    return value

def interval(f,a,b,dx):
    """
    This function creates an interval of form [f(a), f(a+dx), ..., f(b)]
    Arguments    f- any function of a single variable
                    a- left end point on [a,b]
                    b- right end point in [a,b]
                    dx- spacing between coordinates"""
    k = 0
    inter = []
    if dx==0 or (b-a)<dx:
        return inter

    while a+k*dx <= b:
        inter.append(f(a+k*dx))
        k+=1
    return inter

def integrate(i,dx):
    """
    This function takes the integral of the interval using a riemann sum with left endpoints.
    Arguments    i- generated interval
                    dx- spacing between each step"""
    for k in range(len(i)-1):
        if i == []:
            return 0
        else:
            integral = 0
            rect_area = i[k]*dx
            integral += rect_area
    return integral


