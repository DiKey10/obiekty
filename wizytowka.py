from faker import Faker
fake = Faker("pl_PL")

class wizytowka:
    def __init__(self,imie,nazwisko,praca,mail,adres):
        self.imie=imie
        self.nazwisko=nazwisko
        self.praca=praca
        self.mail=mail
        self.adres=adres
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.praca} {self.mail} {self.adres}'
    @property
    def dlugosc_znakow(self):
        return len(self.imie+self.nazwisko)+1
    def contact(self):
        return f'Kontaktuję się z {self.imie} {self.nazwisko} {self.praca} {self.mail}'


wiz1=wizytowka(fake.first_name(),fake.last_name(),fake.job(),fake.email(),fake.address())
wiz2=wizytowka(fake.first_name(),fake.last_name(),fake.job(),fake.email(),fake.address())
wiz3=wizytowka(fake.first_name(),fake.last_name(),fake.job(),fake.email(),fake.address())
wiz4=wizytowka(fake.first_name(),fake.last_name(),fake.job(),fake.email(),fake.address())
wiz5=wizytowka(fake.first_name(),fake.last_name(),fake.job(),fake.email(),fake.address())

zlot_pizzy=[wiz1,wiz2,wiz3,wiz4,wiz5]

for n in zlot_pizzy:
#    print(n)
#    print(n.dlugosc_znakow)
    print(n.contact())





#print(wiz1.__dict__)
#tak sie nie robi
#print(fake.first_name())
#print(fake.last_name())