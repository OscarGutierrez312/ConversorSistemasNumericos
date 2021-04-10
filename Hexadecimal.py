from Decimal import *
from Binary import *
class Hexadecimal():


    def isHexadecimal(self, hex):
        if len(str(hex)) > 1:
            aux=list(str(hex))[0:-1]
        else:
            aux = list(str(hex))[0]
        dom=["1", "2", "3","4","5","6","7","8","9","A", "B", "C", "D", "E", "F", "a", "b", "c","d", "e", "f"]
        for digit in aux:
            if digit not in dom:
                return False
        return True

    def toDecimal(self, hex):
        if len(hex) > 1:
            aux=list(str(hex))[0:-1]
            aux = aux[::-1]
        else:
            aux = list(str(hex))
        num=0
        for i,digit in enumerate(aux):
            if digit == "A":
                num+=10*pow(16, i)
            elif digit == "B":
                num+=11*pow(16, i)
            elif digit == "C":
                num+=12*pow(16, i)
            elif digit == "D":
                num+=13*pow(16, i)
            elif digit == "E":
                num+=14*pow(16, i)
            elif digit == "F":
                num+=15*pow(16, i)
            else:
                num+=int(digit)*pow(16, i)
        return num

    def toBinary(self, hex):
        if len(hex) > 1:
            aux = list(str(hex))[0:-1]
        else:
            aux = list(str(hex))
        n=Decimal()
        bin=""
        for digit in aux:
            aux1=n.toBinary(self.toDecimal(digit))
            mod=len(aux1)%4
            if mod > 0:
                for i in range(4-(mod)):
                    aux1="0"+aux1
            bin+=aux1
        for i in range(4):
            if bin[0] == "0":
                bin=bin[1::]
        return bin

    def toOctal(self, hex):
        return Binary().toOctal(self.toBinary(hex))