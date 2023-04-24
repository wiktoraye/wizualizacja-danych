import numpy as np

panstwo = ["China","Japan","Germany","USA","South Korea","India","Brazil","Mexico","Spain","Russia"]
rok1999 = [0.56,8.1,5.3,5.63,2.36,0.53,1.1,0.99,2.28,0.94]
rok2014 = [19.91,8.27,5.6,4.25,4.12,3.15,2.31,1.91,1.89,1.69]

def oblicz_wzrost_produkcji(produkcja_w_1999, produkcja_w_2014):
    return ((produkcja_w_2014 - produkcja_w_1999) / produkcja_w_1999) * 100

wyniki = []

for i in range(len(panstwo)):
    wzrost_produkcji = oblicz_wzrost_produkcji(rok1999[i], rok2014[i])
    wyniki.append(wzrost_produkcji)
    print(f"Produkcja w kraju {panstwo[i]} wzrosła o {wzrost_produkcji:.2f}%")

x = min(rok1999)
for i in range(len(panstwo)):
    if rok1999[i] == x:
        print(f"{panstwo[i]}: {rok1999[i]} najmniej w 1999")
y = min(rok2014)
for i in range(len(panstwo)):
    if rok2014[i] == y:
        print(f"{panstwo[i]}: {rok2014[i]} najmniej w 2014")

z = max(rok1999)
for i in range(len(panstwo)):
    if rok1999[i] == z:
        print(f"{panstwo[i]}: {rok1999[i]} najwiecej w 1999")
h = max(rok2014)
for i in range(len(panstwo)):
    if rok2014[i] == h:
        print(f"{panstwo[i]}: {rok2014[i]} najwiecej w 2014")

kraje_mniej_produkcji = [panstwo[i] for i in range(len(panstwo)) if rok2014[i] < rok1999[i]]
print("Kraje, które wyprodukowały w 2014 mniej samochodów niż w 1999: ")
for kraj in kraje_mniej_produkcji:
    print(kraj)