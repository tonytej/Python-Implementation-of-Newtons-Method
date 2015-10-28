import sympy
from sympy import *

def gradient(function, xvalue):
	x = symbols('x')
	yprime = diff(function)
	return yprime.subs(x, xvalue)

def tangentline_equation(function, xvalue):
	x = symbols('x')
	function = sympify(function)
	print function
	yvalue = function.subs(x, xvalue)
	print yvalue
	m = gradient(function, xvalue)
	print m
	equation = (m * x - m * xvalue) + yvalue
	return equation


function = "x**2 + 1"
print tangentline_equation(function, 3)