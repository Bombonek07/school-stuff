class M:
    
    pi = 3.14159265358979
    e  = 2.71828182882818
    
    @staticmethod
    def abs(num) -> int:
        if num >= 0:
            return num
        else:
            return (num*(-1))
    
    @staticmethod
    def isEven(num) -> bool:
        if (num%2) == 0:
            return True
        else:
            return False
    
    @staticmethod
    def isOdd(num) -> bool:
        if (num%2) != 0:
            return True
        else:
            return False

    @staticmethod
    def isPositive(num) -> bool:
        if num >= 0:
            return True
        else:
            return False

    @staticmethod
    def isNegative(num) -> bool:
        if num < 0:
            return True
        else:
            return False
    
    @staticmethod
    def isPrimeNumber(num) -> bool:
        prime_num = [2, 3, 5]
        if num in prime_num:
            return True
        else:
            if num%2 != 0:
                if num%3 != 0:
                    if num%5 != 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
      
    @staticmethod
    def isLeapYear(num) -> bool:
        if (num%4) == 0:
            if (num%100) == 0:
                if (num%400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    @staticmethod
    def isPerfectNumber(num) -> bool:
        perfectnumbers = [6, 28, 496, 8128, 8589869056, 137438691328]
        if num in perfectnumbers:
            return True
        else:
            return False
    
    @staticmethod
    def getSumOfDigits(num) -> int:
        num1 = 0
        for x in str(num):
            num1 += int(x) 
        return num1
            

if __name__ == "__main__": 
    num = 97
    print(num)

    print(M.abs(num))
    print(M.isEven(num))
    print(M.isOdd(num))
    print(M.isPositive(num))
    print(M.isNegative(num))
    print(M.isPrimeNumber(num))
    print(M.isLeapYear(num))
    print(M.isPerfectNumber(num))
    print(M.getSumOfDigits(num))
