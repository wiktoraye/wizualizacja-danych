import math
b = 10.51
print(math.ceil(b))
print(math.floor(b))
print(round(b))

x=4.44
y=1.44
def function(x,y):
    if isinstance(x, int) and isinstance(y, int):
        wynik = x % y
        print(wynik)
    elif isinstance(x, float) or isinstance(y, float):
        wynik = math.fmod(x, y)
        print(wynik)
function(x,y)

print("Logarytmy")

a=12
n=10
def function2(a,n):
    for i in range(2,n):
        print(math.log(a,i), end=" | ")
function2(a,n)


print("\n4 kropka")
def function3(a):
    print(math.exp(a))
    print(math.e**a)
    print(math.pow(math.e,a))
function3(a)






