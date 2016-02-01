import sympy
from sympy import *

def gradient(function, xvalue):
	x = symbols('x')
	yprime = diff(function)
	return yprime.subs(x, xvalue)

def tangentline_equation(function, xvalue):
	x = symbols('x')
	function = sympify(function)
	yvalue = function.subs(x, xvalue)
	m = gradient(function, xvalue)
	equation = (m * x - m * xvalue) + yvalue
	return equation

def newton(function, xstart):
	pass


function = "x**2 + 1"
print tangentline_equation(function, 3)