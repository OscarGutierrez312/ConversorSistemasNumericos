
class Decimal():


    def isDecimal(self, num):
        try:
            int(num)
            if(num<0):
                return False
            return True
        except:
            return False

    def toBinary(self, num):
        aux=[]
        if num==0:
            bin="0"
        else:
            while num>0:
                aux.append(num%2)
                num=num//2
            bin="".join([str(a)for a in aux])[::-1]
        return bin

    def toOctal(self, num):
        aux=[]
        if num == 0:
            oct="0"
        else:
            while num>0:
                aux.append(num%8)
                num=num//8
            oct="".join([str(a)for a in aux])[::-1]
        return oct

    def toHexadecimal(self, num):
        aux=[]
        if num == 0:
            hex="0"
        else:
            while num>0:
                res=num%16
                if res == 10:
                    aux.append('A')
                elif res == 11:
                    aux.append('B')
                elif res == 12:
                    aux.append('C')
                elif res == 13:
                    aux.append('D')
                elif res == 14:
                    aux.append('E')
                elif res == 15:
                    aux.append('F')
                else:
                    aux.append(res)
                num = num//16
            hex="".join([str(a)for a in aux])[::-1]
        return hex

