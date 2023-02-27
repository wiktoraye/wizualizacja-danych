print("Stringi")
napis="abcdefghihklmnouprstwzxyb"
print(napis[12])
print(len(napis))
print(napis.count("b"))
print(napis.upper())

print("parzyste indeksy")
print(napis[::2])

print("\nn ostatnich liter")
n=5
print(napis[-n:len(napis)])
print(napis[len(napis)-n:])

print("Odwacanie tekstu")
print(napis[::-1])

print("Ktory dluzszy")
napis1="abcde"
napis2="abcdefg"

if len(napis1)>len(napis2):
    print(napis1)
elif len(napis2)>len(napis1):
    print(napis2)
elif len(napis2)==len(napis1):
    print("Maja taka sama dlugosc")


print("Imie i data urodzenia")
imie="Wiktor"
data_ur="30.08.2003"
nowy=f'My name is {imie} My date of birth is {data_ur}'
print(nowy)

