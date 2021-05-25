import numpy as np

class Interface():
    DICIONARIO_SINAIS = {"a": "+", "b" : "-", "c" : "x", "d" : "÷"}

    def imprimirManualFracao(sinal):
        print(" a     c")
        print("--- ", DICIONARIO_SINAIS[sinal], " ---")
        print(" b     d")

    def pedirFracoes():
        a = float(input("Digite a: "))
        b = float(input("Digite b: "))
        c = float(input("Digite c: "))
        d = float(input("Digite d: "))
        return (a, b, c, d)

    def instrucoesMatriz():
        print("Digite a matriz separando os valores por virgula e as +\
              \nlinhas por colchetes como no exemplo abaixo: ")
        print("[1, 2, 3], [4, 5, 6], [7, 8, 9]")
        print("linha 1 = [1, 2, 3]")
        print("linha 2 = [4, 5, 6]")
        print("linha 3 = [7, 8, 9]")

    def pedirMatriz(letra):
        matriz = eval(input("Digite a matriz ", letra, " 3x3: "))
        return matriz

    def mostrarOpcoes():
        print("a. Soma de duas frações")
        print("b. Subtração de duas frações")
        print("c. Multiplicação de duas frações")
        print("d. Divisão de duas frações")
        print("e. Soma de duas matrizes 3 × 3")
        print("f. Multiplicação de duas matrizes 3 × 3")
        opcao = input("Digite a letra minuscula da opcao: ")
        return opcao

    def mostrarResultadoFracao(resultado):
        print(resultado)
        

class Main():

    def inicializar():
        opcao = Inteface.mostraOpcoes()
        if opcao == ("a" or "b" or "c" or "d"):
            Interface.imprimirManualFracao(opcao)
            valores = Interface.pedirFracoes()
            fracoes = Calculadora.calcularFracoes(valores)
            resultado = self.calculoFracoes(opcao, fracoes)
            Interface.mostrarResultado(resultado)

        elif opcao == "e" or opcao == "f":
            Interface.instrucoesMatriz()
            matrizA = Interface.pedirMatriz("A")
            matrizB = Interface.pedirMatriz("B")
            np.array(matrizA)
            np.array(matrizB)
            resultado = self.calculoMatriz(opcao, matrizA, matrizB)
            Interface.mostrarResultado(resultado)
        else:
            Interface.opcaoInvalida()
    
    def calculoFracoes(opcao, fracoes):
        fracaoA = fracoes[0]
        fracaoB = fracoes[1]
        if opcao == "a":    
            resultado = Calculadora.somarFracoes(fracaoA, fracaoB)
        elif opcao == "b":
            resultado = Calculadora.subtrairFracoes(fracaoA, fracaoB)
        elif opcao == "c":
            resultado = Calculadora.multiplicarFracoes(fracaoA, fracaoB)
        else:
            resultado = Calculadora.dividirFracoes(fracaoA, fracaoB)
        return resultado

    def calculoMatriz(opcao, matrizA, matrizB):
        if !(Utils.validaMatriz(matrizA) and Utils.validaMatriz(matriz)):
            Interface.matrizInvalida()
        else:
            if opcao == "e":
                return Calculadora.somarMatrizes(matrizA, matrizB)
            else:
                return Calculadora.multiplicarMatrizes(matrizA, matrizB)

class Claculadora():

    def calcularFracoes(tuplaValores):
        fracaoA = tuplaValores[0] / tuplaValores[1]    
        fracaoB = tuplaValores[2] / tuplaValores[3]
        return (fracaoA, fracaoB)

    def somarFracoes(facaoA, fracaoB):
        return fracaoA + fracaoB

    def subtrairFracoes(facaoA, fracaoB):
        return fracaoA - fracaoB
    
    def multiplicarFracoes(facaoA, fracaoB):
        return fracaoA * fracaoB

    def dividirFracoes(facaoA, fracaoB):
        return fracaoA / fracaoB

    def multiplicarMatrizes(matrizA, matrizB):
        return np.dot(matrizA, matrizB) 

    def somarMatrizes(matrizA, matrizB):
        return np.add(matrizA, matrizB)

class Utils():

    def validaTamanhoLinhaMatriz(matriz):
        if len(matriz) == 3:
            return True
        return False

    def validaTamanhoColunaMatriz(matriz):
        for linha in matriz():
            if len(linha) != 3:
                return False
        return True

    def validaMatriz(matriz):
        if validaTamanhoLinhaMatriz:
            if validaTamanhoColunaMatriz:
                return True
        return False