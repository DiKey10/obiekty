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
    def label_length(self):
        return len(self.imie+self.nazwisko)+1

    def contact(self):
        return f'Kontaktuję się z {self.imie} {self.nazwisko} {self.praca} {self.mail}'


class BaseContact(wizytowka):
    def __init__(self, fone , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fone=fone
    def contact(self):
        return f'Wybieram numer {self.fone} i dzwonie do {self.imie} {self.nazwisko}'
class BusinessContact(wizytowka):
    def __init__(self, workfone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.workfone=workfone
    def contact(self):
        return f'Wybieram numer {self.workfone} i dzwonie do {self.imie} {self.nazwisko}'

x=''
ilosc=''
def create_contact(x,ilosc):
    print("Wybierz rodzaj (normal = 1/biznes = 2) i ilosc wizytowek")
    for x in range(ilosc):
        if x == 1:
            kontakt = BaseContact(fake.phone_number(), fake.first_name(), fake.last_name(), fake.job(), fake.email(),
                        fake.address())
            print(kontakt)
        elif x== 2:
            kontakt = BusinessContact(fake.phone_number(), fake.first_name(), fake.last_name(), fake.job(), fake.email(),
                        fake.address())
            print(kontakt)
        else:
            print("Miales wybrac normal lub biznes")

print(create_contact(x=2,ilosc=3))

"""
osoba1 = BaseContact(fake.phone_number(),fake.first_name() , fake.last_name() ,  fake.job(), fake.email(),fake.address())
osoba2=BaseContact(fake.phone_number(),fake.first_name() , fake.last_name() ,  fake.job(), fake.email(),fake.address())
osoba3=BusinessContact(fake.phone_number(),fake.first_name() , fake.last_name() ,  fake.job(), fake.email(),fake.address() )

osoba4=BusinessContact(workfone="+48 508094821",imie="zbyszek",nazwisko=fake.last_name(), praca=fake.job(),mail="dsa@dksa.pl",adres=" tutaj")

print(osoba4.contact())
print(osoba4.label_length)
#print(wiz1.__dict__)
#tak sie nie robi
#print(fake.first_name())
#print(fake.last_name())

"""