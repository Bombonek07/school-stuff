class test: 
    def __init__(self, operace, what, txt, txt2):
        self.__operace = operace
        self.__what = what
        self.__txt = txt
        self.__txt2 = txt2
    def input(self, operace, what, txt, txt2):
        self.__operace = operace
        self.__what = what
        self.__txt = txt
        self.__txt2 = txt2

        while self.__what not in self.__operace:
            if self.__what == "":
                print(f"{self.__txt2} not defined\n{70*'-'}")
                self.__what = str(input(f"výběr {self.__txt}:({', '.join(self.__operace)}) or 'break'\n"))
            elif self.__what == "break":
                exit()
            elif self.__what not in self.__operace:
                print(f"this {self.__txt2} is not an option\n{70*'-'}")
                self.__what = str(input(f"výběr {self.__txt}:({', '.join(self.__operace)}) or 'break'\n"))
        else:
            print(f"{self.__txt2} set\n{70*'-'}")
