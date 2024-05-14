class calculadora:
    def __init__(self):
        pass
    def soma(self, num1, num2):
        return num1+num2
    def subtracao(self, num1, num2):
        return num1-num2
    def multiplicacao(self, num1, num2):
        return num1*num2
    def divisao(self, num1, num2):
       if num2 != 0:
            return num1/num2
       else:
           return("Pode não")
minhac= calculadora()
resultado1= minhac.soma(2, 2)
resultado2= minhac.subtracao(2, 2)
resultado3= minhac.multiplicacao(2, 2)
resultado4= minhac.divisao(2, 0)


print("Soma:", resultado1)
print("Subtração:", resultado2)
print("Mutiplicação:", resultado3)
print("Divisão:", resultado4)