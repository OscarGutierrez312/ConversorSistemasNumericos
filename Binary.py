
class Binary():


    def isBinary(self, bin):
        aux=list(str(bin))
        for digit in aux:
            if (int(digit) < 0) or (int(digit) > 1):
                return False
        return True

    def toDecimal(self, bin):
        aux=list(str(bin)[::-1])
        num=0
        for i,digit in enumerate(aux):
            if digit == '1':
                num+=pow(2, i)
        return num

    def toOctal(self, bin):
        aux=list(str(bin))
        mod=len(aux)%3
        oct=""
        if mod > 0:
            for i in range(3-mod):
                aux.insert(0, '0')
        for i in range(len(aux)//3):
            aux1="".join(aux[i*3:(i*3)+3])
            oct+=str(self.toDecimal(aux1))
        return oct

    def toHexadecimal(self, bin):
        aux=list(str(bin))
        mod=len(aux)%4
        hex=""
        if mod > 0:
            for i in range(4-mod):
                aux.insert(0, '0')
        for i in range(len(aux)//4):
            aux1="".join(aux[i*4:(i*4)+4])
            res=self.toDecimal(aux1)
            if res == 10:
                hex+='A'
            elif res == 11:
                hex+='B'
            elif res == 12:
                hex+='C'
            elif res == 13:
                hex+='D'
            elif res == 14:
                hex+='E'
            elif res == 15:
                hex+='F'
            else:
                hex+=str(res)
        return hex