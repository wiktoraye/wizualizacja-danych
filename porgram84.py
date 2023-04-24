import numpy as np

imiona = ["Anna","Zofia","Sylwia","Katarzyna","Teresa","Toamsz","Cezary","Zenon","Filip","Adrian"]
wiek = [21,40,13,31,34,14,13,28,20,15]
plec = ["K","K","K","K","K","M","M","M","M","M"]
waga = [65,80,64,69,74,61,66,61,69,77]
wzrost = [179,179,151,177,170,157,151,153,160,160]
okulary = ["NIE","TAK","NIE","TAK'","NIE","TAK","NIE","TAK","NIE","TAK"]

imiona = ["Anna","Zofia","Sylwia","Katarzyna","Teresa","Toamsz","Cezary","Zenon","Filip","Adrian"]
sorted_imiona = sorted(imiona)  # Sort the imiona list alphabetically
print(sorted_imiona)

noszacy_okulary = []
for i in range(len(imiona)):
    if okulary[i] == "TAK":
        noszacy_okulary.append(imiona[i])
print(noszacy_okulary)

kobiety_w_wieku_20_30 = []
for i in range(len(imiona)):
    if plec[i] == "K" and 20 <= wiek[i] <= 30:
        kobiety_w_wieku_20_30.append(imiona[i])
print(kobiety_w_wieku_20_30)

osoby_w_przedziale = []
for i in range(len(imiona)):
    if  okulary[i] == "NIE" and 60 <= waga[i] <= 80 and 160 <= wzrost[i] <= 180:
        osoby_w_przedziale.append(imiona[i])
print(osoby_w_przedziale)

bmi = []
for i in range(len(waga)):
    wzrost_m = wzrost[i] / 100
    bmi_i = waga[i] / (wzrost_m ** 2)
    bmi_i_rounded = round(bmi_i, 2)
    bmi.append(bmi_i_rounded)
print(bmi)

sredni_wiek = sum(wiek) / len(wiek)
najblizsze_imiona = []
najmniejsza_roznica_wieku = None
for i in range(len(wiek)):
    roznica_wieku = abs(wiek[i] - sredni_wiek)
    if najmniejsza_roznica_wieku is None or roznica_wieku < najmniejsza_roznica_wieku:
        najblizsze_imiona = [imiona[i]]
        najmniejsza_roznica_wieku = roznica_wieku
    elif roznica_wieku == najmniejsza_roznica_wieku:
        najblizsze_imiona.append(imiona[i])

print("Średni wiek:", sredni_wiek)  # Wyświetl średni wiek
print("Imię lub imiona osoby lub osób, które są najbliżej średniego wieku:", najblizsze_imiona)


