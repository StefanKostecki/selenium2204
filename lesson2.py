# from selenium import webdriver
# przegladarka = webdriver.Chrome()
# przegladarka.get('http://wp.pl')


class Czlowiek:    #klasa jest szablonem (przepisem), z którego powstaje obiekt (danie)
    gatunek = 'homo sapiens'
    # cialo klasy
    def __init__(self, imie):
        """Metoda inicjalizacyjna"""
        print('Tworze nowego Czlowieka o imieniu', imie)
        self.imie = imie

    def przedstaw_sie(self):
        print('Hej, jestem', self.imie)


class Dziecko(Czlowiek):
    pass


# instancja klasy
adam = Czlowiek('Adam')  #adam.imie = "Adam"
ewa = Czlowiek('Ewa')     #ewa.imie = "Ewa"
print(adam)
print(type(adam))
print(type(ewa))
print(dir(adam))

print(adam.imie)
print(ewa.imie)

adam.przedstaw_sie()

kain = Dziecko('Kain')
kain.przedstaw_sie()

# wynik = isinstance(adam, Czlowiek)
# print(wynik)
#
# napis = str('hej')
# print(napis)
# print(type(napis))
# print(dir(napis))
# print(napis.count('gh'))
# print(napis.upper())