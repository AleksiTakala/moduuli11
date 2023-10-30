class Auto:
    def __init__(self, rkt, hn):
        self.rkt = rkt
        self.hn = hn
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.hn:
            self.nopeus = self.hn
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunti):
        self.kuljettu += self.nopeus * tunti

    def tulosta(self):
        print(f'Rekisteritunnus{self.rkt}, Huippunopeus {self.hn}kmh, Nykyinen nopeus {self.nopeus}kmh, Kuljettu matka {self.kuljettu}km')
class sähköauto(Auto):
    def __init__(self,  rkt, hn, akku):
        self.akku = akku
        super().__init__(rkt, hn)
    def tulosta(self):
        super().tulosta()
        print(f"Akku kapasiteetti {self.akku}")
class polttoauto(Auto):
    def __init__(self, rkt, hn, bensatankki):
        self.bensatankki = bensatankki
        self.nopeus = 0
        super().__init__(rkt, hn)
    def tulosta(self):
        super().tulosta()
        print(f"Bensa kapasiteetti {self.bensatankki}")


SA = sähköauto("ABC-15", 180, "52.5kwh")
PA = polttoauto("ACD-123", 160, "32,3l")
SA.kiihdytä(100)
PA.kiihdytä(120)
SA.kulje(3)
PA.kulje(3)
SA.tulosta()
PA.tulosta()