list1=[1,2,3,4,5,6,7,8,9,10]
list2=[10,20,30,40,50,60,70,80,90,100]
list3=[]
print(list1+list2)
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(list3)
miesiace = ["Grudzien","Maj","Lipiec","Luty"]
def funkcja(a):
    if a == "Styczen":
        return 0
    elif a == "Luty":
        return 1
    elif a == "Marzec":
        return 2
    elif a == "Kwiecien":
        return 3
    elif a == "Maj":
        return 4
    elif a == "Czerwiec":
        return 5
    elif a == "Lipiec":
        return 6
    elif a == "Sierpien":
        return 7
    elif a == "Wrzesien":
        return 8
    elif a == "Listopad":
        return 10
    elif a == "Pazdziernik":
        return 9
    elif a == "Grudzien":
        return 11

miesiace.sort(key=funkcja)
print(miesiace)

nazwiska = ["Jakacki", "Hryniewicz", "Wisniewski", "Andrut"]
litera="H"
listnazwisk = []
def funkcja2(nazwiska,litera):
    for i in range(0,len(nazwiska)):
        if nazwiska[i][0]>litera:
            listnazwisk.append(nazwiska[i])
funkcja2(nazwiska,litera)
print(listnazwisk)

listnazwisk2 = []
def funkcja3(nazwiska):
    nazwiska = [x for x in nazwiska if len(x) > 6]
    print(nazwiska)
funkcja3(nazwiska)


slowo="aabbaa"
def palindrom(slowo):
    wynik=True
    for i in range(0,len(slowo)):
        if(slowo[i]!=slowo[len(slowo)-i]):
            wynik=False
            return wynik
if(palindrom(slowo)==True):
    print("Jest to palindrom")
elif(palindrom(slowo)==False):
    print("Nie jest to palindrom")




