import numpy as np

my_array = np.array(range(10, 40, 2))
print(my_array)
my_array.resize(10)
print(my_array)

for i in range(len(my_array)):
    my_array[i] += 3
print(my_array)

for i in range(len(my_array)):
    my_array[i] *= 2
print(my_array)

for i in range(len(my_array)):
    if my_array[i] % 6 == 2:
        my_array[i]=0
print(my_array)

def change(A,x):
    B=A.copy()
    for i in range(len(B)):
        if B[i] == 0:
            B[i] = x
    return B
print(change(my_array,69))

macierz1 = np.array([[1, 1, 2],[2, 1, 0],[4, 1, 2]])
macierz2 = np.array([[2, 5, 8],[2, 8, 0],[4, 3, 1]])

print(np.add(macierz1,macierz2))
print(np.dot(macierz1,macierz2))
print(macierz1*macierz2)

print(macierz1.T)
print(np.linalg.inv(macierz1))
print(np.power(macierz1,5))
print(np.linalg.det(macierz1))

print(np.power(np.linalg.inv(macierz1),3))
c = ([[1],[2],[3]])
d = ([2,5,7])
print(np.dot(d,c))
print(np.add(c,d))

e = ([[1,5],[2,1]])
f = ([[2,1],[2,8]])
print(np.divide(e,f))
