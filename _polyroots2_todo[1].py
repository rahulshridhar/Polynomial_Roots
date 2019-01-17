
'''
module: _polyroots2_todo.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on roots of polynomials
- implemented from algorithms/pseudocode provided
'''

import cmath, numpy as np
import _polyroots_todo

def bairstow(a, r=0, s=0, es100=.5, imax=1000, debug=False, tab=14, precision=7):
    "performs one iteration of bairstow's method; i.e. locates two roots only"
    #a: polynomial a
    #r: initial guess for coefficient -r in x**2 -r*x - s
    #s: initial guess for coefficient -s in x**2 -r*x - s
    #es100: error tolerance (%)
    #imax: max # of iterations
    #debug: True: display iterations; False: silent mode
    #tab: #spaces for tabulated output; 0: disable
    #precision: # of significant digits for float values
    n = len(a)-1  #n is degree of polynomial a
    if n < 3:  #polynomial must be degree 3 or larger
        return None
    r = float(r); s = float(s)
    a = np.array(a, dtype=float)
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    iter = 0
    ea1 = ea2 = 1.  #100%
    dr = ds = .0
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","dr","ds","r","s","ea1(%)","ea2(%)",t=tab))
    while True:
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                   else "iter={}, dr={:.{p}}, ds={:.{p}}, r={:.{p}}, s={:.{p}}, ea1={:.{p}%}, ea2={:.{p}%}")
                  .format(iter, dr, ds, r, s, ea1, ea2, t=tab, p=precision))
        if (ea1*100 < es100 and ea2*100 < es100) or iter > imax: break
        iter += 1
        b[n] = a[n]
        b[n-1] = a[n-1] + r * b[n]
        c[n] = b[n]
        c[n-1] = b[n-1] + r * c[n]
        for i in range(n - 2, -1, -1):
            b[i] = a[i] + r * b[i+1] + s * b[i+2]
            c[i] = b[i] + r * c[i+1] + s * c[i+2]
        det = c[2] * c[2] - c[3] * c[1]
        if det != 0:
            dr = (-b[1] * c[2] + b[0] * c[3]) / det
            ds = (-b[0] * c[2] + b[1] * c[1]) / det
            r = r + dr
            s = s + ds
            if r != 0:
                ea1 = abs(dr/r) * 100
            if s != 0:
                ea2 = abs(ds/s) * 100
        else:
            r = r+1
            s = s+1
            iter = 0
        #TODO: finish implementation from algorithm in textbook, p.191
    #end while
    #a = b[2:n+1].copy() #optional: we can deplete polynomial a here and pass it back to find more roots
    return _polyroots_todo.quadratic(1, -r, -s)
#end bairstow()