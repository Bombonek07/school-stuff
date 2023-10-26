class Cypher:
    def __init__(self, amount = 3):
        self.__number_of_rails = amount
    
    def __transcript(self, open_text):
        return open_text.replace(" ","")
    
    def encrypt(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__rails = [[] for _ in range(self.__number_of_rails)]
        self.__encrypt_text = ''
        num = 0
        count = 0

        for x in self.__open_text:
            if count == 0:     
                self.__rails[num].append(x)
                num += 1

                if num == self.__number_of_rails:
                    count = 1
                    num = self.__number_of_rails-2

            elif count == 1:    
                self.__rails[num].append(x)
                num -= 1

                if num == -1:
                    count = 0
                    num = 1

        for m_list in self.__rails:
            for leater in m_list:
                self.__encrypt_text += leater

        return self.__encrypt_text
    
    def decrypt(self, cypher_text):
        self.__cypher_text = cypher_text
        self.__rail = [['\n' for i in range(len(self.__cypher_text))]
                for j in range(self.__number_of_rails)]
     
        dir_down = None
        row, col = 0, 0

        for i in range(len(self.__cypher_text)):
            if row == 0:
                dir_down = True
            if row == self.__number_of_rails - 1:
                dir_down = False
         
            self.__rail[row][col] = '*'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(self.__number_of_rails):
            for j in range(len(self.__cypher_text)):
                if ((self.__rail[i][j] == '*') and
                (index < len(self.__cypher_text))):
                    self.__rail[i][j] = self.__cypher_text[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(self.__cypher_text)):
            if row == 0:
                dir_down = True

            if row == self.__number_of_rails-1:
                dir_down = False
             
            if (self.__rail[row][col] != '*'):
                result.append(self.__rail[row][col])
                col += 1
             
            if dir_down:
                row += 1
            else:
                row -= 1
        return("".join(result))

    def get_open_text(self):
        pass
    
    def get_cypher_text(self):
        pass
    
    def __str__(self):
        pass

print(Cypher(2).encrypt("GEEKS FOR GEEKS"))
print(Cypher(2).decrypt("GESOGESEKFREK"))