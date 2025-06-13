'''
 Name: Connor Kouznetsov
 Description: Week 9 Lecture 2 Oct 24th
'''

#lambda functions - smasll anonymous functions can take any number of arguments, but can only have one expression
val = lambda n: n + 5
print(val(10))

def add5 (n):
    return n + 5

print(add5(14))

maxval = lambda a, b: a if a >= b else b
print(maxval(5, 6))

def multiples(v: float, a: int) -> list[float]:
    mult = []
    for i in range(1, a + 1):
        mult.append(v * i)
    return mult

vlist = multiples(5, 10)
print(vlist)

#HURRICANE #2 STARTS