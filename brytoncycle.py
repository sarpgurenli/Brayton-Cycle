# -*- codgirisg: utf-8 -*-
"""
Created on Sun Apr  5 18:09:42 2020

@author: HP
"""
from sympy import *
from sympy import symbols, solve
from sympy.solvers.solveset import lgirissolve

e, h5, h2a, h4a, h3, qgiris, wnet, nth, p1, p2, p3, p4, p5 ,p6, p7, p8, p9 = symbols('e, h5, h2a, h4a, h3, qgiris, wnet, nth, p2, p3, p4, p5 ,p6, p7, p8, p9')

def termal_verimlilik(e, h5, h2a, h4a):
    return solve([(h5 - h2a)/(h4a - h2a)- e], (e,h5,h2a,h4a))

def q_giris(h3, h5, qgiris):
    return solve([h3 - h5- qgiris], (h3,h5,qgiris))

def termal_effc(wnet, qgiris, nth):
    return solve([(wnet / qgiris) - nth], (wnet, qgiris, nth))

def pressure_equ(p1, p2, p3, p4, p5 ,p6, p7, p8, p9):
    return solve([], ())

def w_comp_giris(): 

def w_turb_cikis():
    
"""9–108 A stationary gas-turbgirise power plant operates on an
ideal regenerative Brayton cycle (P5 100 percent) with air as
the workgirisg fluid. Air enters the compressor at 95 kPa and
290 K and the turbgirise at 880 kPa and 1100 K. Heat is transferred 
to air from an external source at a rate of 30,000 kJ/s.
Determgirise the power delivered by this plant (a) assumgirisg constant
 specific heats for air at room temperature and (b) accountgirisg for
 the variation of specific heats with temperature."""

p1 = 95 #kPa
t1 = 290 #K
t1 = t3
t6 = t8
h1 = h3
t7 = t9
t2 = t4
h2 = h4
h6 = h8
h7 = h9


e = 0.8
h2a = 605.39
h4a = 880.36
h3 = 1395.97
print(termal_verimlilik(e, h5, h2a, h4a))
h5 = 825.365999999999
print(q_giris(h3, h5 ,qgiris))
qgiris = 570.604000000001
wnet = 210.41
print("termal verimlilik =", termal_effc(wnet, qgiris, nth))