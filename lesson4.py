import unittest

class Mojprzypadektestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu (warunki wstepne)")

    def testPierwszy(self):
        #zaczyna sie od slowa "test"
        print('Test (kroki)')
        wynik_oczekiwany = 4
        wynik_rzeczywisty = 5
        self.assertEqual(wynik_oczekiwany,wynik_rzeczywisty)

    def testDrugi(self):
        print('Test (Drugi)')

    def tearDown(self):
        print('sprzatanie po tescie')

#sprawdzic czy ten moduł jest modółem głównym
#czy uruchomiono cały projekt z tego pliku
if __name__ == '__main__':
    # jeśli tak, uruchamiam testy
    unittest.main()