# Zad1
import datetime

a = 4
b = 8

print(a + b)
print(b - a)
print(a * b)
print(a / b)

# Zad2
imie = input("Podaj imię")

print("Witaj " + imie)

# Zad3
print(float(input("Podaj pierwsza liczbe")) + float(input("Podaj druga liczbe")))

# Zad4
suma = 0

for n in range(8, 80):
    suma += n

print(suma)

print(sum(range(8,80)))

# Zad5
from datetime import date
print(date.fromisoformat("2023-06-06") - date.today())

Zad6
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
dzialanie = input("Podaj działanie: ")

if dzialanie == 'dodawanie':
    print(a + b)
elif dzialanie == 'odejmowanie':
    print(a - b)
elif dzialanie == 'mnożenie':
    print(a * b)
elif dzialanie == 'dzielenie':
    print(a / b)
else:
    print("Niepoprawne działanie")





