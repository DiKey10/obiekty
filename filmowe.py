import random


class Film:
    def __init__(self, tytul, rok_produkcji, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_produkcji = rok_produkcji
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        # Variables
        self._ilosc_odtworzen = 0

    @property
    def play(self):
        self._ilosc_odtworzen += 1
        return self._ilosc_odtworzen

    def __str__(self):
        return f'{self.tytul} ({self.rok_produkcji}) '


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f'{self.tytul} S{self.numer_sezonu:02d}E{self.numer_odcinka:02d} '

    def sorted(self):
        return sorted(self.tytul)


film1=Film("IT", 2021, "horror", 1)
film2=Film("Bodygard", 1999, "Dramat", 0)
serial1=Serial(23, 5, "GoT", 2020, "fantasy", 0)
serial2=Serial(8, 3, "Ty", 2020, "fantasy", 1)


biblioteka= [film1,film2,serial1,serial2]


def generate_views(x):
    n=random.randint(1,100)
    x.liczba_odtworzen = n


for item in biblioteka:
    if isinstance(item,Serial):
        print(item)
    else:
        print(item)

for petla in range(10):
    randomowo = random.choice(biblioteka)
    generate_views(randomowo)


print(randomowo.liczba_odtworzen)
generate_views(randomowo)
for film in biblioteka:
    print(film.__dict__)


print(random.choice(biblioteka))

