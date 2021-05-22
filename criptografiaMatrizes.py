import numpy as np
import math


def interface():
    while True:
        print("1. discriptografar")
        print("2. criptografar")
        print("3. testar a matriz")
        print("4. Parar o programa:")
        op = int(input("Digite a opção: "))
        if op == 1:
            chave = eval(input("Digite a matriz chave: "))
            matriz = eval(input("Digite a matriz criptografada: "))
            print(discriptografar(chave, matriz))

        elif op == 2:
            chave = eval(input("Digite a matriz chave: "))
            frase = input("Digite a frase: ")
            print(criptografar(chave, frase))
        
        elif op == 3:
            chave = eval(input("Digite a matriz chave: "))
            inversivel(chave, True)

        elif op == 4:
            break

        else:
            print("Opção inválida!!!!")
        print("\n")


def inversivel(mat, mostrar=False):
    identidade = [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]
    np.array(mat)
    inversa = np.linalg.inv(mat)
    result = np.dot(mat,inversa)
    for i in range(3):
        if list(result[i]) != list(identidade[i]):
            print("Não é inversível")
            print(result)
            return False
    if mostrar == True:
        print(inversa)    
    return True
            
def criptografar(chave, frase):    
    if inversivel(chave) == True:
        num = len(frase) / 3
        if len(frase) % 3 == 0: 
            num = int(num)
            mensagem = []
            lista = []
            for i in range(num):
                lista.append(ord(frase[i]))
            mensagem.append(lista)
            lista = []
            for i in range(num, num * 2):
                lista.append(ord(frase[i]))
            mensagem.append(lista)
            lista = []
            for i in range(num*2, num*3):
                lista.append(ord(frase[i]))
            mensagem.append(lista)    
            chave = np.array(chave)
            mensagem = np.array(mensagem)
            print("Mensagem na tebela ASCII:\n",mensagem)
            result = np.dot(chave, mensagem)
            print("\nMensagem criptografada:")
            return result 
        else: 
            return "A frase não é divisivel por 3"
    else:
        return "A matriz chave não é inversível"

def discriptografar(chave, lista):
    if inversivel(chave) == True:
        num = len(lista[0])
        lista = np.array(lista)
        chave = np.array(chave)
        chave = np.linalg.inv(chave)
        print("Matriz Inversa:")
        print(chave)
        result = np.dot(chave,lista)
        print("\nMensagem tabela ASCII:")
        print(result)
        print("\n")
        frase = ""
        for cont in range(3):
            for i in range(num):
                a = round(result[cont][i])
                a = int(a)
                frase += chr(a) 
        return frase
    else: 
        return "A matriz chave nâo é inversível" 

if __name__ == "__main__":
    interface()