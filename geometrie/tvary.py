unit = ["mm", "cm", "dm", "m", "km"]
shape = ["ctverec", "triangle", "rectangle", "square"]

class jednotky:
    def __init__(self, j="cm"):
        self.__jednotky = j

    def setunit(self, j="cm"):
        self.__jednotky = j
        if self.__jednotky == "":
            self.__jednotky = "cm"
            return "unit is not definite(set to default = cm)"
        elif self.__jednotky not in unit:
            self.__jednotky = "cm"
            return "trhis unit is not an option(set to default = cm)"
        else:
            self.__jednotky = j
            return "unit set"

class tvar:
    def __init__(self, t="ctverec"):
        self.__tvar = t

    def setshape(self, t="ctverec"):
        self.__tvar = t
        if self.__tvar == "":
            self.__tvar = "ctverec"
            return "shape is not definite"
        elif self.__tvar not in shape:
            return "trhis shape is not an option"
        
        if self.__tvar == "ctverec":
            kocka = ctverec(int(input("déla strany 'a': ")))
            what = str(input("obvod nebo obsah?:"))
            if what == "obvod":
                kocka.obvod()
                return kocka.getobvod()
            elif what == "obsah":
                kocka.obsah()
                return kocka.getobsah()
            else:
                return "nic"

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
        return self.__obvod

    def getobsah(self):
        return (self.__obsah,"²")
        
print(jednotky().setunit(str(input("jednotka ve které budete zadávat hodnoty\nvýběr(mm, cm, dm, m, km)\n"))))
print(tvar().setshape(str(input("tvar kderý chceš\nvýběr(ctverec, triangle, rectangle, square)\n"))))

