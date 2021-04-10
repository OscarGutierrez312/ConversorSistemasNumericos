from Decimal import *
from Binary import *

class Octal():

    def isOctal(self, oct):
        aux=list(str(oct))
        for digit in aux:
            if (int(digit) < 0) or (int(digit) > 7):
                return False
        return True

    def toDecimal(self, oct):
        aux=list(str(oct)[::-1])
        num=0
        for i,digit in enumerate(aux):
            num+=int(digit)*pow(8, i)
        return num

    def toBinary(self, oct):
        aux=list(str(oct))
        n=Decimal()
        bin=""
        for digit in aux:
            aux1=n.toBinary(int(digit))
            mod=len(aux1)%3
            if mod > 0:
                for i in range(3-(mod)):
                    aux1="0"+aux1
            bin+=aux1
        for i in range(3):
            if bin[0] == "0":
                bin=bin[1::]
        return bin

    def toHexadecimal(self, oct):
        return Binary().toHexadecimal(self.toBinary(oct))