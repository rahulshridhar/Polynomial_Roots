
'''
module: _polyroots_todo.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on roots of polynomials
- implemented from algorithms/pseudocode provided
'''

import math, numpy as np, cmath

def quadratic(a, b, c):
    a = complex(a)
    b = complex(b)
    c = complex(c)
    "returns the two roots for quadratic equation a*x**2 + b*x + c"
    #TODO:
    #  modify so that it returns real roots (w/o imaginary part), or
    #  complex roots (w/ both real and imaginary parts, if applicable)
    disc = b*b - 4*a*c

    rad = cmath.sqrt(disc)

    d1, d2 = b + rad, b - rad
    xr1 = -2*c / (d1 if abs(d1) > abs(d2) else d2)
    xr2 = -2*c / (d2 if abs(d1) > abs(d2) else d1)
    if (disc.real>=0 and disc.imag==0):
        return xr1.real, xr2.real
    else:
        return xr1, xr2
#end quadratic()

def muller(f, xr, h, es100=.5, imax=1000, debug=False, tab=14, precision=7):
    "performs one iteration of muller's method; i.e. locates one root only"
    #f: function f(x)
    #xr: first initial guess
    #h: step-size to perturb xr
    #es100: error tolerance (%)
    #imax: max # of iterations
    #debug: True: display iterations; False: silent mode
    #tab: #spaces for tabulated output; 0: disable
    #precision: # of significant digits for float values
    x2 = xr = float(xr)
    x1 = float(xr + h)
    x0 = float(xr - h)
    iter = 0
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","x0","x1","x2","xr","ea(%)",t=tab))
    while True:
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}%}" if tab
                   else "iter={}, x0={:.{p}}, x1={:.{p}}, x2={:.{p}}, xr={:.{p}}, ea={:.{p}%}")
                  .format(iter, x0, x1, x2, xr, ea, t=tab, p=precision))
        if ea*100 < es100 or iter > imax: break
        iter += 1
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        dxr = quadratic(a, b = a*h1 + d1, c = f(x2))[0]
        xr = x2 + dxr
        if xr: ea = abs(dxr / xr)
        x0, x1, x2 = x1, x2, xr
    #end while
    return xr
#end muller()