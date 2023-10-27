unit = ["mm", "cm", "dm", "m", "km"]
shape = ["ctverec", "obdelnik", "trojuhelnik", "kruh", "krychle", "kvadr", "jehlan", "koule", "kuzel", "valec"]

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
    def __init__(self, t=""):
        self.__tvar = t

    def setshape(self, t=""):
        self.__tvar = t

        while self.__tvar not in shape:
            if self.__tvar == "":
                print(f"shape is not definite\n{70*'-'}")
                self.__tvar = str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)})\n"))
            elif self.__tvar not in shape:
                print(f"trhis shape is not an option\n{70*'-'}")
                self.__tvar = str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)})\n"))
        
        if self.__tvar == "ctverec":
            TVAR = ctverec(int(input(f"{70*'-'}\ndéla strany 'a': ")))
            what = str(input("obvod nebo obsah?:"))
            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()
            else:
                return "nic"
        
        if self.__tvar == "obdelnik":
            TVAR = obdelnik(int(input(f"{70*'-'}\ndéla strany 'a': ")), int(input(f"déla strany 'b': ")))
            what = str(input("obvod nebo obsah?:"))
            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()
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

class obdelnik:
    def __init__(self, a=0, b=0):
        self.__strana_a = a
        self.__strana_b = b

    def setside(self, a=0, b=0):
        self.__strana_a = a
        self.__strana_b = b
    
    def obvod(self):
        self.__obvod = (self.__strana_a*2)+(self.__strana_b*2)

    def obsah(self):
        self.__obsah = self.__strana_a*self.__strana_b

    def getobvod(self):
        return f"{70*'-'}\nobvod obdelniku je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"{70*'-'}\nobsah obdelniku je: {self.__obsah}{units.getunit()}²\n{70*'-'}"
    
units = jednotky()
print(units.setunit(str(input(f"jednotka ve které budete zadávat hodnoty\nvýběr({', '.join(unit)})\n"))))
print(tvar().setshape(str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)})\n"))))

