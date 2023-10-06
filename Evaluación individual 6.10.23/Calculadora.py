class Calculadora:
    def suma(self, a,b):
        return a+b

    def resta(self,a,b):
        return a-b

    def multipli(self,a,b):
        return a*b

    def dividir(self,a,b):
        if b == 0:
            print("Sintaxis Error.")
            return None
        else:
            return a/b

if __name__ == "__main__":
    calculadora = Calculadora()

    num1 = int(input("Digite el primer numero entero: "))
    num2 = int(input("Digite el segundo numero entero: "))

    print("Suma:",calculadora.sumar(num1,num2))
    print("Resta:",calculadora.restar(num1,num2))
    print("Multiplicacion:",calculadora.multiplicar(num1,num2))

    resultado_division=calculadora.dividir(num1,num2)
    if resultado_division is not None:
        print("División:",resultado_division)