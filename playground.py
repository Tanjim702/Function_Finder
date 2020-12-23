filtered_list = [[46, 33, -75, 1], [-13, -108, 76], [-95, 184], [279]]
import math
from sympy import *
x,y,z = symbols('x y z')
init_printing(use_unicode=True)

def factorial(num):
    val = 1
    n = num
    while n != 0:
        val = val * n
        n = n -1
    return val 
def factorial_of_exp(num):
    exp = ''
    n = num
    while n != 0:
        exp = exp + '(x-{n})*'.format(n=n)
        n =n-1
    # sympied = sympify(exp[:-1])
    return  exp[:-1]

def getFinalExpr():
    expr = '1'
    for arr in filtered_list:
        arrIndex = filtered_list.index(arr)
        deno = factorial(arrIndex+1)
        mult = arr[0]
        if mult>0:
            loopexpr = '(+{0}*'.format(mult)+'{}'.format(factorial_of_exp(arrIndex+1)) + '/{0})'.format(deno)
        else:
            loopexpr = '({0}*'.format(mult)+ '{}'.format(factorial_of_exp(arrIndex+1)) + '/{0})'.format(deno)

        expr = expr + '+({0})'.format(loopexpr)
        # expr = expr[:-1]
    print(expr)    
    expr = sympify(expr)
    expr = factor(expr)
    print(expr)
        
getFinalExpr()        