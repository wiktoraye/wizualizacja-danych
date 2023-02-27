def nwd(x,y):
    if x > y:
        for i in range(x, 0, -1):
            if y % i == 0:
                print(i)
                break

    elif x < y:
        for i in range(y, 0, -1):
            if x % i == 0:
                print(i)
                break

print("Podaj 2 liczby calkowite")
n = int(input())
m = int(input())
nwd(n, m)