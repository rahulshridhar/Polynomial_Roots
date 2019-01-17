#script: topic6.4.py
#author: Rahul Shridhar

import matplotlib.pyplot as plt
import _poly, _plot, _polyroots_todo

#x**4 - 2x**3 + 6x**2 -2x + 5
a = [ 5, -2, 6, -2, 1 ]

def f(x): return _poly.eval(a, x)

xl, xu = -1.25, 2.25
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)))

prec = 4

xr1 = _polyroots_todo.muller(f, xr=5, h=.5, es100=.5*10**(2-prec), debug=True, tab=18, precision=prec)
print("xr1 = {:.{p}}".format(xr1, p=prec))

#we can find the remaining roots by finding xr1 conjugate first, then depleting
#polynomial a with resulting quadratic polynomial (x - xr1)(x - xr2), then
#continue applying muller() until we get a quadratic or linear equation,
#which then can be solved with the quadratic formula or simple solving.
xr2 = xr1.conjugate()
print("xr2 = {:.{p}}".format(xr2, p=prec))

#Deflate the polynomial by dividing by the two roots found above
b = _poly.defl(a, xr1)[0]
c = _poly.defl(b, xr2)[0]

xr3, xr4 = _polyroots_todo.quadratic(a = c[2], b = c[1], c = c[0])
print("xr3 = {}".format(xr3))
print("xr4 = {}".format(xr4))

#plot roots
xr = [xr1, xr2, xr3, xr4]  #add additional roots here
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  #get current axes object and obtain dimensions
left, right = axes.get_xlim(); width = right - left
down, up = axes.get_ylim(); height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i+1, xr[i], p=prec),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width/25, (i+1)*height/25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()