unit = ["mm", "cm", "dm", "m", "km"]
shape = ["ctverec", "triangle", "rectangle", "square"]

class jednotky:
    def __init__(self, j="cm"):
        self.__jednotky = j

    def setunit(self, j="cm"):
        self.__jednotky = j
        if self.__jednotky == "":
            self.__jednotky = "cm"
        elif self.__jednotky not in unit:
            self.__jednotky = "cm"
            return f"trhis unit is not an option(set to default = cm)\n{70*'-'}"
        else:
            self.__jednotky = j
            return f"unit set\n{70*'-'}"
        
    def getunit(self):
        return self.__jednotky

class tvar:
    def __init__(self, t="ctverec"):
        self.__tvar = t

    def setshape(self, t="ctverec"):
        self.__tvar = t

        while self.__tvar not in shape:
            if self.__tvar == "":
                print(f"shape is not definite\n{70*'-'}")
                self.__tvar = str(input("tvar kderý chceš\nvýběr(ctverec, triangle, rectangle, square)\n"))
            elif self.__tvar not in shape:
                print(f"trhis shape is not an option\n{70*'-'}")
                self.__tvar = str(input("tvar kderý chceš\nvýběr(ctverec, triangle, rectangle, square)\n"))
        
        if self.__tvar == "ctverec":
            kocka = ctverec(int(input(f"{70*'-'}\ndéla strany 'a': ")))
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
        return f"{70*'-'}\nobvod ctverce je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"{70*'-'}\nobsah ctverce je: {self.__obsah}{units.getunit()}²\n{70*'-'}"

units = jednotky()
print(units.setunit(str(input("jednotka ve které budete zadávat hodnoty\nvýběr(mm, cm, dm, m, km)\n"))))
print(tvar().setshape(str(input("tvar kderý chceš\nvýběr(ctverec, triangle, rectangle, square)\n"))))

