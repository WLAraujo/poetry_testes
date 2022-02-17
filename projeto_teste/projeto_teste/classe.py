class Calculadora:

    def soma(self,x,y):
        return x+y

    def subtracao(self,x,y):
        return x-y

    def multiplicacao(self,x,y):
        return x*y

    def divisao(self,x,y):
        if y == 0:
            return("Não aprendeu nada na escola não???")
        else:
            return x/y