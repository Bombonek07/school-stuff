from math import sqrt
import math

unit = ["mm", "cm", "dm", "m", "km"]
shape = ["ctverec", "obdelnik", "trojuhelnik", "kruh", "krychle", "kvadr"] # "jehlan", "koule", "kuzel", "valec"

class jednotky:
    def __init__(self, j=""):
        self.__jednotky = j

    def setunit(self, j=""):
        self.__jednotky = j

        while self.__jednotky not in unit:
            if self.__jednotky == "":
                print(f"unit not defined\n{70*'-'}")
                self.__jednotky = str(input(f"jednotka ve které budeteš zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))
            elif self.__jednotky == "break":
                exit()
            elif self.__jednotky not in unit:
                print(f"trhis unit is not an option\n{70*'-'}")
                self.__jednotky = str(input(f"jednotka ve které budeteš zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))
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
            what = str(input(f"{70*'-'}\nvýběr operace:({', '.join(operace)}) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
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
            a = int(input("délka strany 'a': "))
            b = int(input("délka strany 'b': "))

            while a==0 or b==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                a = int(input("délka strany 'a': "))
                b = int(input("délka strany 'b': "))

            TVAR = obdelnik(a, b)
            what = str(input(f"{70*'-'}\nvýběr operace:({', '.join(operace)}) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")

            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()
        
        if self.__tvar == "trojuhelnik":
            operace = ["obvod", "obsah", "strana"]
            a, b, c = 0, 0, 0
            what = str(input(f"výběr operace:({', '.join(operace)}(pravoúhlého △)) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}(pravoúhlého △)) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}(pravoúhlého △)) or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")

            if what == "obvod":
                a = int(input("délka strany 'a': "))
                b = int(input("délka strany 'b': "))
                c = int(input("délka strany 'c': "))

                while a==0 or b==0:
                    print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                    a = int(input("délka strany 'a': "))
                    b = int(input("délka strany 'b': "))
                    c = int(input("délka strany 'c': "))
                
                TVAR = trojuhelnik(a, b, c)
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                a = int(input("délka základny 'a': "))
                v = int(input("délka výšky    'v': "))
                while a==0 or b==0:
                    print(f"{70*'-'}\ncan not be a 0\n{70*'-'}")
                    a = int(input("délka základny 'a': "))
                    v = int(input("délka výšky    'v': "))

                TVAR = trojuhelnik(a, v)
                TVAR.obsah()
                return TVAR.getobsah()
            elif what == "strana":
                print("u strany kterou potřebuješ zadej 0")
                a = int(input("délka odvěsny 'a': "))
                b = int(input("délka odvěsny 'b': "))
                c = int(input("délka přepona 'c': "))
                while (a==0 and b==0)or(a==0 and c==0)or(b==0 and c==0)or(a==0 and c<=b)or(b==0 and c<=a):
                    print(f"{70*'-'}\ntwo sides can not by a 0 or přepona < odvěsna\n{70*'-'}\nstranu kterou potřebuješ zadej 0")
                    a = int(input("délka odvěsny 'a': "))
                    b = int(input("délka odvěsny 'b': "))
                    c = int(input("délka přepony 'c': "))

                TVAR = trojuhelnik()
                TVAR.setside_strana(a, b, c)
                TVAR.strana()
                return TVAR.getstrana()
            
        if self.__tvar == "kruh":
            operace = ["obvod", "obsah"]
            r = int(input("déla průměru 'r': "))

            while r==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                r = int(input("déla průměru 'r': "))

            TVAR = kruh(r)
            what = str(input(f"{70*'-'}\nvýběr operace:({', '.join(operace)}) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")
            
            if what == "obvod":
                TVAR.obvod()
                return TVAR.getobvod()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()

        if self.__tvar == "krychle":
            operace = ["plocha", "obsah"]
            a = int(input("déla strany 'a': "))

            while a==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                a = int(input("déla strany 'a': "))

            TVAR = krychle(a)
            what = str(input(f"{70*'-'}\nvýběr operace:({', '.join(operace)}) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")
            
            if what == "plocha":
                TVAR.plocha()
                return TVAR.getplocha()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()

        if self.__tvar == "kvadr":
            operace = ["plocha", "obsah"]
            a = int(input("délka strany 'a': "))
            b = int(input("délka strany 'b': "))
            c = int(input("délka strany 'c': "))

            while a==0 or b==0 or c==0:
                print(f"{70*'-'}\nside can not be a 0\n{70*'-'}")
                a = int(input("délka strany 'a': "))
                b = int(input("délka strany 'b': "))
                c = int(input("délka strany 'c': "))

            TVAR = kvadr(a, b, c)
            what = str(input(f"{70*'-'}\nvýběr operace:({', '.join(operace)}) or 'break'\n"))

            while what not in operace:
                if what == "":
                    print(f"operation not defined\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
                elif what == "break":
                    exit()
                elif what not in operace:
                    print(f"this operation is not an option\n{70*'-'}")
                    what = str(input(f"výběr operace:({', '.join(operace)}) or 'break'\n"))
            else:
                print(f"operation set\n{70*'-'}")

            if what == "plocha":
                TVAR.plocha()
                return TVAR.getplocha()
            elif what == "obsah":
                TVAR.obsah()
                return TVAR.getobsah()
            
class ctverec:
    def __init__(self, a=0):
        self.__strana = a

    def setside(self, a=0):
        self.__strana = a
    
    def obvod(self):
        self.__obvod = round(self.__strana*4, 3)

    def obsah(self):
        self.__obsah = round(self.__strana**2, 3)

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
        self.__obvod = round((self.__strana_a*2)+(self.__strana_b*2), 3)

    def obsah(self):
        self.__obsah = round(self.__strana_a*self.__strana_b, 3)

    def getobvod(self):
        return f"obvod obdelniku je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"obsah obdelniku je: {self.__obsah}{units.getunit()}²\n{70*'-'}"
    
class trojuhelnik:
    def __init__(self, a=0, b=0, c=0, v=0):
        self.__strana_a = a
        self.__strana_b = b
        self.__strana_c = c
        self.__vyska = v

    def setside_obvod(self, a=0, b=0, c=0):
        self.__strana_a = a
        self.__strana_b = b
        self.__strana_c = c
    
    def setside_obsah(self, a=0, v=0):
        self.__strana_a = a
        self.__vyska = v

    def setside_strana(self, a=0, b=0, c=0):
        self.__strana_a = a
        self.__strana_b = b
        self.__strana_c = c
        
    def obvod(self):
        self.__obvod = round(self.__strana_a+self.__strana_b+self.__strana_c, 3)

    def obsah(self):
        self.__obsah = round(0.5*self.__strana_a*self.__vyska, 3)

    def strana(self):
        if self.__strana_a == 0:
            self.__abc = "odvěsny 'a'"
            self.__strana = round(sqrt((self.__strana_c**2)-(self.__strana_b**2)), 3)
        elif self.__strana_b == 0:
            self.__abc = "odvěsny 'b'"
            self.__strana = round(sqrt((self.__strana_c**2)-(self.__strana_a**2)), 3)
        elif self.__strana_c == 0:
            self.__abc = "přepony 'c'"
            self.__strana = round(sqrt((self.__strana_a**2)+(self.__strana_b**2)), 3)

    def getobvod(self):
        return f"obvod trojuhelniku je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"obsah trojuhelniku je: {self.__obsah}{units.getunit()}²\n{70*'-'}"
    
    def getstrana(self):
        return f"{70*'-'}\ndélka {self.__abc}: {self.__strana}{units.getunit()}\n{70*'-'}"

class kruh:
    def __init__(self, r=0):
        self.__polomer = r

    def setpolomer(self, r=0):
        self.__polomer = r
    
    def obvod(self):
        self.__obvod = round(self.__polomer*2*math.pi, 3)

    def obsah(self):
        self.__obsah = round(math.pi*(self.__polomer**2), 3)

    def getobvod(self):
        return f"obvod kruhu je: {self.__obvod}{units.getunit()}\n{70*'-'}"

    def getobsah(self):
        return f"obsah kruhu je: {self.__obsah}{units.getunit()}²\n{70*'-'}"
    
class krychle:
    def __init__(self, a=0):
        self.__strana = a

    def setside(self, a=0):
        self.__strana = a
    
    def plocha(self):
        self.__plocha = round(6*(self.__strana**2), 3)

    def obsah(self):
        self.__obsah = round(self.__strana**3, 3)

    def getplocha(self):
        return f"plocha krychle je: {self.__plocha}{units.getunit()}²\n{70*'-'}"

    def getobsah(self):
        return f"obsah krychle je: {self.__obsah}{units.getunit()}³\n{70*'-'}"
    
class kvadr:
    def __init__(self, a=0, b=0, c=0):
        self.__strana_a = a
        self.__strana_b = b
        self.__strana_c = c

    def setside(self, a=0, b=0, c=0):
        self.__strana_a = a
        self.__strana_b = b
        self.__strana_c = c
    
    def plocha(self):
        self.__plocha = round(((self.__strana_a*self.__strana_b)*2)+((self.__strana_a*self.__strana_c)*2)+((self.__strana_b*self.__strana_c)*2), 3)

    def obsah(self):
        self.__obsah = round(self.__strana_a*self.__strana_b*self.__strana_c, 3)

    def getplocha(self):
        return f"plocha kvadru je: {self.__plocha}{units.getunit()}²\n{70*'-'}"

    def getobsah(self):
        return f"obsah kvadru je: {self.__obsah}{units.getunit()}³\n{70*'-'}"

units = jednotky()
print(units.setunit(str(input(f"jednotka ve které budete zadávat hodnoty\nvýběr({', '.join(unit)}) or 'break'\n"))))
print(tvar().setshape(str(input(f"tvar kderý chceš\nvýběr({', '.join(shape)}) or 'break'\n"))))