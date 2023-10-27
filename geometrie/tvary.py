unit = ["mm", "cm", "dm", "m", "km"]
shape = ["ctverec", "obdelnik", "trojuhelnik", "kruh", "krychle", "kvadr", "jehlan", "koule", "kuzel", "valec"]

class jednotky:
    def __init__(self, j=""):
        self.__jednotky = j

    def setunit(self, j=""):
        self.__jednotky = j

        while self.__jednotky not in unit:
            if self.__jednotky == "":
                print(f"unit not defined\n{70*'-'}")
                self.__jednotky = str(input(f"jednotka ve které budete zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))
            elif self.__jednotky == "break":
                exit()
            elif self.__jednotky not in unit:
                print(f"trhis unit is not an option\n{70*'-'}")
                self.__jednotky = str(input(f"jednotka ve které budete zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))
        else:
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
                self.__tvar = str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)}) or 'break'\n"))
            elif self.__tvar == "break":
                exit()
            elif self.__tvar not in shape:
                print(f"trhis shape is not an option\n{70*'-'}")
                self.__tvar = str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)}) or 'break'\n"))
        else:
            print(f"shape set\n{70*'-'}")
        
        if self.__tvar == "ctverec":
            operace = ["obvod", "obsah"]
            a = int(input("déla strany 'a': "))

            while a==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                a = int(input("déla strany 'a': "))

            TVAR = ctverec(a)
            what = str(input("obvod nebo obsah? or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input("obvod nebo obsah? or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input("obvod nebo obsah? or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")
            
            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()
        
        if self.__tvar == "obdelnik":
            operace = ["obvod", "obsah"]
            a = int(input("déla strany 'a': "))
            b = int(input("déla strany 'b': "))

            while a==0 or b==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                a = int(input("déla strany 'a': "))
                b = int(input("déla strany 'b': "))

            TVAR = obdelnik(a, b)
            what = str(input("obvod nebo obsah? or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input("obvod nebo obsah? or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input("obvod nebo obsah? or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")

            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()

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
        return f"obvod ctverce je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"obsah ctverce je: {self.__obsah}{units.getunit()}²\n{70*'-'}"

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
        return f"obvod obdelniku je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"obsah obdelniku je: {self.__obsah}{units.getunit()}²\n{70*'-'}"
    
units = jednotky()
print(units.setunit(str(input(f"jednotka ve které budete zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))))
print(tvar().setshape(str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)}) or 'break'\n"))))

