import numpy as np

class Interface():

    def __init__(self):
        self.DICIONARIO_SINAIS = {"a": "+", "b" : "-", "c" : "x", "d" : "÷"}

    def imprimir_manual_fracao(self, sinal):
        print(" a       c")
        print("--- ", self.DICIONARIO_SINAIS[sinal], " ---")
        print(" b       d")

    def pedir_fracoes(self):
        a = float(input("Digite a: "))
        b = float(input("Digite b: "))
        c = float(input("Digite c: "))
        d = float(input("Digite d: "))
        return (a, b, c, d)

    def instrucoes_matriz(self):
        print("Digite a matriz separando os valores por virgula e as +\
              \nlinhas por colchetes como no exemplo abaixo: ")
        print("[1, 2, 3], [4, 5, 6], [7, 8, 9]")
        print("linha 1 = [1, 2, 3]")
        print("linha 2 = [4, 5, 6]")
        print("linha 3 = [7, 8, 9]")

    def pedir_matriz(self):
        matriz = eval(input("Digite a matriz 3x3: "))
        return matriz

    def mostrar_opcoes(self):
        print("a. Soma de duas frações")
        print("b. Subtração de duas frações")
        print("c. Multiplicação de duas frações")
        print("d. Divisão de duas frações")
        print("e. Soma de duas matrizes 3 × 3")
        print("f. Multiplicação de duas matrizes 3 × 3")
        opcao = input("Digite a letra minuscula da opcao: ")
        return opcao

    def mostrar_resultado(self, resultado):
        print(resultado)

    def opcao_invalida(self):
        print("opcao inválida!")
        

class Main():

    def __init__(self):
        self.interface = Interface()
        self.calculadora = Claculadora()

    def inicializar(self):
        opcao = self.interface.mostrar_opcoes()
        if opcao == "a" or opcao == "b" or opcao == "c" or opcao == "d":
            self.interface.imprimir_manual_fracao(opcao)
            valores = self.interface.pedir_fracoes()
            fracoes = self.calculadora.calcular_fracoes(valores)
            resultado = self.calculo_fracoes(opcao, fracoes)
            self.interface.mostrar_resultado(resultado)

        elif opcao == "e" or opcao == "f":
            self.interface.instrucoes_matriz()
            matriz_a = self.interface.pedir_matriz()
            matriz_b = self.interface.pedir_matriz()
            np.array(matriz_a)
            np.array(matriz_b)
            resultado = self.calculo_matriz(opcao, matriz_a, matriz_b)
            self.interface.mostrar_resultado(resultado)
        else:
            self.interface.opcao_invalida()
    
    def calculo_fracoes(self, opcao, fracoes):
        fracao_a = fracoes[0]
        fracao_b = fracoes[1]
        if opcao == "a":    
            resultado = self.calculadora.somar_fracoes(fracao_a, fracao_b)
        elif opcao == "b":
            resultado = self.calculadora.subtrair_fracoes(fracao_a, fracao_b)
        elif opcao == "c":
            resultado = self.calculadora.multiplicar_fracoes(fracao_a, fracao_b)
        else:
            resultado = self.calculadora.dividir_fracoes(fracao_a, fracao_b)
        return resultado

    def calculo_matriz(self, opcao, matriz_a, matriz_b):
        if not(Utils().valida_matriz(matriz_a) and Utils().valida_matriz(matriz_b)):
            self.interface.matriz_invalida()
        else:
            if opcao == "e":
                return self.calculadora.somar_matrizes(matriz_a, matriz_b)
            else:
                return self.calculadora.multiplicar_matrizes(matriz_a, matriz_b)

class Claculadora():

    def calcular_fracoes(self, tupla_valores):
        fracao_a = tupla_valores[0] / tupla_valores[1]    
        fracao_b = tupla_valores[2] / tupla_valores[3]
        return (fracao_a, fracao_b)

    def somar_fracoes(self, fracao_a, fracao_b):
        return fracao_a + fracao_b

    def subtrair_fracoes(self, fracao_a, fracao_b):
        return fracao_a - fracao_b
    
    def multiplicar_fracoes(self, fracao_a, fracao_b):
        return fracao_a * fracao_b

    def dividir_fracoes(self, fracao_a, fracao_b):
        return fracao_a / fracao_b

    def multiplicar_matrizes(self, matriz_a, matriz_b):
        return np.dot(matriz_a, matriz_b) 

    def somar_matrizes(self, matriz_a, matriz_b):
        return np.add(matriz_a, matriz_b)

class Utils():

    def valida_tamanho_linha_matriz(self, matriz):
        if len(matriz) == 3:
            return True
        return False

    def valida_tamanho_coluna_matriz(self, matriz):
        for linha in matriz:
            if len(linha) != 3:
                return False
        return True

    def valida_matriz(self, matriz):
        if self.valida_tamanho_linha_matriz(matriz) and  self.valida_tamanho_coluna_matriz(matriz):
                return True
        return False

if __name__ == "__main__":
    main = Main()
    main.inicializar()