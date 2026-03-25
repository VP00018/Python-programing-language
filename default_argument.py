<<<<<<< HEAD
"""
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
"""

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

=======
"""
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
"""

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

>>>>>>> c221da442758ed131598f2b393070929f837904f
count(0, 10)