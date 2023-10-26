class Hráč():
    def __init__(self, vyška):
        self.vyška = vyška

    def GetVyška(self):
        return f"Vyška hráče je {self.vyška} cm."
    
    def SetPozice(self, pozice):
        self.__pozice = pozice

    def GetPozice(self):
        return f"Pozice hráče je {self.__pozice}."
        

hrač1 = Hráč(12)

hrač1.SetPozice("Záchod")
print(hrač1.pozice)
print(hrač1.GetPozice())
