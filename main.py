
from tkinter import *
from tkinter import ttk
from Decimal import *
from Binary import *
from Octal import *
from Hexadecimal import *

opt=('Decimal', 'Binario', 'Octal', 'Hexadecimal')

class setFrame(Toplevel):

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.__label1 = Label(self, text="De:")
        self.__label2 = Label(self, text="A:")
        self.__label3 = Label(self, text="Numero:")
        self.__label4 = Label(self, text="Resultado:")
        self.__txtResult = Label(self, text="")

        self.__label1.config(font=("Helvetica", 15))
        self.__label2.config(font=("Helvetica", 15))
        self.__label3.config(font=("Helvetica", 15))
        self.__label4.config(font=("Helvetica", 15))

        self.__op1 = ttk.Combobox(self, width=30)
        self.__op1['values'] = opt

        self.__op2 = ttk.Combobox(self, width=30)
        self.__op2['values'] = opt

        self.__txt1 = Text(self, height=2.5, width=30)

        self.__calc = Button(self, text="Convertir", width=12)
        self.__btnExit = Button(self, text="Salir", width=7)

        self.__label1.grid(row=1, column=1, padx=10, pady=10)
        self.__label2.grid(row=1, column=2, padx=10, pady=10)

        self.__op1.grid(row=2, column=1, padx=10, pady=10)
        self.__op2.grid(row=2, column=2, padx=10, pady=10)

        self.__label3.grid(row=3, column=1, padx=10, pady=10)
        self.__txt1.grid(row=3, column=2, padx=10, pady=10)

        self.__calc.grid(row=4, column=2, padx=10, pady=10)

        self.__label4.grid(row=5, column=1, padx=10, pady=10)
        self.__txtResult.grid(row=5, column=2, padx=10, pady=10)

        self.__btnExit.grid(row=6, column=1, padx=10, pady=10)

    def setResult(self, result):
        self.__txtResult['text'] = result
        self.__txtResult.config(font=("Helvetica", 15))

    def setType1(self, type):
        self.__label3['text'] = type

    def setType2(self, type):
        self.__label4['text'] = type

    def getOp1(self):
        return self.__op1.get()

    def getOp2(self):
        return self.__op2.get()

    def getInput(self):
        return self.__txt1.get('1.0', END)

    def getCalcButton(self):
        return self.__calc

    def getBtnExit(self):
        return self.__btnExit

class Converter():

    def __init__(self, root):
        self.__root = root
        self.__frame = setFrame(root)
        self.__frame.getCalcButton().configure(command=self.convert)
        self.__frame.getBtnExit().configure(command=self.exit)

    def convert(self):
        numSis = self.__frame.getOp1()
        conv = self.__frame.getOp2()
        correct=False
        try:
            num = int(self.__frame.getInput())
        except:
            num = self.__frame.getInput()

        error = "Entrada Incorrecta"

        self.__frame.setType1(numSis)

        if numSis == 'Decimal':
            result = Decimal()
            correct=result.isDecimal(num)
        elif numSis == 'Binario':
            result = Binary()
            correct = result.isBinary(num)
        elif numSis == 'Octal':
            result = Octal()
            correct = result.isOctal(num)
        elif numSis == 'Hexadecimal':
            result = Hexadecimal()
            correct = result.isHexadecimal(num)
        else:
            self.__frame.setResult("Sistema Numérico Origen No Seleccionado")

        if correct:
            if numSis == conv:
                self.__frame.setResult(num)
                self.__frame.setType2(conv)
            elif conv == 'Decimal':
                self.__frame.setResult(result.toDecimal(num))
                self.__frame.setType2(conv)
            elif conv == 'Binario':
                self.__frame.setResult(result.toBinary(num))
                self.__frame.setType2(conv)
            elif conv == 'Octal':
                self.__frame.setResult(result.toOctal(num))
                self.__frame.setType2(conv)
            elif conv == 'Hexadecimal':
                self.__frame.setResult(result.toHexadecimal(num))
                self.__frame.setType2(conv)
            else:
                self.__frame.setResult("Sistema Numérico Destino No Seleccionado")
        elif numSis == "":
            self.__frame.setResult("Sistema Numérico Origen No Seleccionado")
        else:
            self.__frame.setResult(error)

    def exit(self):
        self.__frame.destroy()
        self.__root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    root.title("Conversor de Sistemas Numericos")
    root.geometry("400x400")
    app = Converter(root)
    root.mainloop()


