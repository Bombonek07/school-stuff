class jednotky:
    def __init__(self, j="cm"):
        self.__jednotky = j

    def setunit(self, j="cm"):
        self.__jednotky = j
        if self.__jednotky == "":
            self.__jednotky = "cm"
            return "shape is not definite(set to default = cm)"
        elif self.__jednotky != "mm"or"cm"or"dm"or"m"or"km":
            self.__jednotky = "cm"
            return "trhis unit is not an option(set to default = cm)"
        else:
            self.__jednotky = j

class tvar:
    def __init__(self, t="ctverec"):
        self.__tvar = t

    def setshape(self, t="ctverec"):
        self.__tvar = t
        if self.__tvar == "":
            self.__tvar = "ctverec"
            return "shape is not definite"
        elif self.__tvar != "ctverec" or "triangle" or "rectangle" or "square":
            return "trhis shape is not an option"
        
        if self.__tvar == "ctverec":
            pass

class ctverec:
    def __init__(self, a=0):
        self.__strana = a

    def setside(self, a=0):
        self.__strana = a
    
    def obvod(self):
        self.__obvod = self.__strana*4

    def obsah(self):
        self.__obsah = self.__strana**2

    def getobvod(self):
        return (self.__obvod)

    def getobsah(self):
        return (self.__obsah,"²")
        
jednotky().setunit(str(input("jednotka ve které budete zadávat hodnoty\nvýběr(mm, cm, dm, m, km)\n")))
tvar().setshape(str(input("tvar kderý chceš\nvýběr(ctverec, triangle, rectangle, square)\n")))

asdfghjklertzuierthjk