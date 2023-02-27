import math
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c=math.gcd(a, b)
a/=c
b/=c
print(a,"/",b)
