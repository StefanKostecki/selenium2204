def dodaj_advanced(*args):
    wynik = 0
    for arg in args:
        wynik = wynik + arg
    return wynik
print(dodaj_advanced(3,4,100))