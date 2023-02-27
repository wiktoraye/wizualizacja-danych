import math
def funkcja(n):
    e1=(1 + (1 / n ))**n
    e2=0
    for x in range(0, n):
        e2 = e2 + 1/math.factorial(x)
    print("e1 −math.e=", e1-math.e)
    print("e2 −math.e=", e2-math.e)
    print("|e1 −math.e|=", abs(e1 - math.e))
    print("|e2 −math.e|=", abs(e2 - math.e))

l = int(input("Podaj liczbe calkowita n:"))
funkcja(l)
