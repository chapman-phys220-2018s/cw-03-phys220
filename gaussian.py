#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def g(x):
    value = (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)
    return value

def interval(f,a,b,dx):
    k = 0
    inter = []
    while a+k*dx <= b:
        inter.append(f(a+k*dx))
        k+=1
    return inter

def integrate(i,dx):
    for k in range(len(i)+1):
        integral = 0
        rect_area = i(k)*dx
        integral += rect_area
    return integral