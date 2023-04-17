def print_unique_values(my_list):
    unique_values = set(my_list)
    for value in unique_values:
        print(value)
list = [5,2,1,5,2]
print_unique_values(list)

my_string = "To be or not to be, that is the question."
my_string = "".join(filter(str.isalpha, my_string))  # usuwanie spacji i innych symboli
for i in range(3, len(my_string), 4):
    print(my_string[i], end="")
print()

def fibonacci(n):
    if n<=1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def fibonacci2(n):
    if n <= 1:
        return n
    pom1=1
    pom2=0

    for i in range(2, n + 1):
        pom3=pom1+pom2
        pom2=pom1
        pom1=pom3
    return pom3
for i in range(10):
    print(fibonacci2(i))

def fun4(n,*args):
    wynik=1
    for num in args:
        wynik=wynik*(num**n)
    return wynik
wynik = fun4(2, 1, 2, 3, 4, 5)
print(wynik)

owoce = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']

def ulubo(words_list):
    owoce2 = [owoc for owoc in owoce if 'u' in owoc or 'o' in owoc]
    return owoce2
print(ulubo(owoce))

def newton(n,k):
    licznik=1
    mianownik=1
    for i in range(1,n+1):
        licznik=licznik*i

    for i in range(1,k+1):
        mianownik=mianownik*i

    for i in range(1,n-k+1):
        mianownik=mianownik*i

    return licznik/mianownik

print(newton(5,2))