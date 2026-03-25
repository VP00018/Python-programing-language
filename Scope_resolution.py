# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in

"""
from math import e

def func1():
    print(e)
e = 3

func1()

"""

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
 
