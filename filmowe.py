
class film:
    def __init__(self, tytul, rok_produkcji, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_produkcji = rok_produkcji
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        # Variables
        self._ilosc_odtworzen = 0
    @property
    def play(self):
        return self._ilosc_odtworzen
        _ilosc_odtworzen = _ilosc_odtworzen + 1
    def __str__(self):
        return f'{self.tytul} ({self.rok_produkcji}) '

class serial(film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f'{self.tytul} S{self.numer_sezonu:02d}E{self.numer_odcinka:02d} '


film1=film("IT",2021,"horror",1)
film2=film("Bodygard",1999,"Dramat",0)
serial1=serial(23,5,"GoT",2018-2020,"fantasy",0)
serial2=serial(8,3,"Ty",2018-2020,"fantasy",1)

print(serial2)
