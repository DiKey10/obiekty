from faker import Faker
fake = Faker("pl_PL")

class wizyt:
    def __init__(self,imie,nazwisko,mail):
        self.imie=imie
        self.nazwisko=nazwisko
        self.mail=mail

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.mail}'
    @property
    def dlugosc(self):
        return len(self.imie+self.nazwisko) +1
    def kont(self):
        return f'Kontaktuje sie z {self.imie} {self.nazwisko} pracuje jako {self.mail}'


osoba1 = wizyt(fake.first_name() , fake.last_name() , fake.email())
osoba2=wizyt(fake.first_name(),fake.last_name(),fake.email())
osoba3=wizyt(fake.first_name(),fake.last_name(),fake.email())

anty_bigos=[osoba1,osoba2,osoba3]

for n in anty_bigos:
    print(n.dlugosc)
    print(n.kont())