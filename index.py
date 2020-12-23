import math
from sympy import *
x,y,z = symbols('x y z')
iterable_list = [1,3,5,7,8,4,6,7,-99]
main_list = []
filtered_list = []
init_printing()
def get_new_list(arr):
    new_list = []
    for num in range(0,len(arr)-1):
        val = arr[num+1]-arr[num]
        new_list.append(val) 
    main_list.insert(len(main_list),new_list)

def filter_list_from_empty_values(arr):
    for array in arr:
        if len(array) != 0:
            filtered_list.append(array)


def find_all_lists(arr):
    for num in arr:
        if len(main_list) == 0:
            get_new_list(arr)
        get_new_list(main_list[len(main_list)-1])
    filter_list_from_empty_values(main_list)
    return filtered_list    

find_all_lists(iterable_list)
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
    expr = '{}'.format(iterable_list[0])
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
    expr = sympify(expr)
    return expr
        
last = factor(getFinalExpr())
pprint(last,use_unicode=True)