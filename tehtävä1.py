class kirja:
    def __init__(self, nimi, kirjoittaja, sivumr):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumr = sivumr
    def tulosta(self):
        print(f"{self.nimi}, {self.kirjoittaja}, {self.sivumr}")
class lehti:
    def __init__(self, toimittaja, nimi):
        self.toimittaja = toimittaja
        self.nimi = nimi
    def tulosta(self):
        print(f"{self.nimi}, {self.toimittaja}")
kirjat = []
kirjat.append(lehti("Aku ankka", " Aki hyyppä"))
kirjat.append(kirja("Hytti no.6", "Rosa Liksom", 200))

for i in kirjat:
    i.tulosta()