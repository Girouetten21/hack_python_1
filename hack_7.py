"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    array = []
    i = 5
    while i >= 0:
        array.append(i)
        i -= 1
    return array