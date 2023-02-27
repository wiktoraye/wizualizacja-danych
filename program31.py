import math

list1 = []
for i in range(0,14):
    list1.append(i**5)
print(list1)

list2 = []
for i in range(1,20):
    list2.append(math.factorial(i))
print(list2)

list3 = []
for i in range (0,20):
    list3.append(math.pow(math.e,i))
print(list3)

list4 = ["Jakacki", "Hryniewicz", "Wisniewski", "Andrut"]
listn = []
for i in range(0,len(list4)):
    listn.append(len(list4[i]))
print(listn)

