import matplotlib.pyplot as plt
import math
import numpy as np

def seno(a, b, valor):
    s = math.sin(valor)
    y = a + b * s
    return y 

def cosseno(a, b, valor):
    c = math.cos(valor)
    y = a + b * c
    return y

def tangente(a, b, valor):
    t = math.tan(valor)
    y = a + b * t 
    return y

def periodo(c):
    periodo = 2 * math.pi / np.absolute(c)
    return periodo

def img(a, b):
    imagem = []
    imagem.append(a - b)
    imagem.append(a + b)
    return imagem

def lado_y(a, b, c, d, p):
    x = np.arange(0, p*2, 0.001)
    sen = []
    cos = []
    tan = []
    lx = len(x)
    for i in range(lx):
        valor = c * x[i] + d
        sen.append(seno(a, b, valor))
        cos.append(cosseno(a, b, valor))
        # tan.append(tangente(a, b, valor))
    if lx == len(sen) and lx == len(cos):
        return (sen, cos, tan, x)
    else:
        return False

def lado_y_tan(a, b, c, d):
    p = c/math.pi
    per = 2*p
    x = np.arange(0, per, 0.001)
    y = []
    for i in range(len(x)):
        valor = c * x[i] + d
        y.append(tangente(a,b,valor))
    return (x, y, p)

def amplitude(img):
    amp = (img[1] - img[0]) / 2
    return amp

def calcular(a, b, c, d):
    p = periodo(c)
    y = lado_y(a, b, c, d, p)
    x = y[3]
    image = img(a, b)
    amp = amplitude(image)
    result = "Periodo: " + str(p) + "\nImagem: " + str(image) + "\nAmplitude: " + str(amp)
    return (y, x, result)

def plotar(x, y):
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    a = eval(input("Digite a: "))
    b = eval(input("Digite b: "))
    c = eval(input("Digite C: "))
    d = eval(input("Digite d: "))
    i = 0
    while i == 0: 
        print("1. Grafíco Seno")
        print("2. Gráfico Cosseno")
        print("3. Gráfico Tangente")
        print("4. Digitar outros valores")
        print("5. Parar o programa")
        op = input("Digite a opção: ")
        calculo = calcular(a, b, c, d)
        y = calculo[0]
        x = calculo[1]
        result = calculo[2]
        if op == "1":
            y = y[0]
            plt.title(result)
            plotar(x, y)
        elif op == "2":
            y = y[1]
            plt.title(result)
            plotar(x, y)
        elif op == "3":
            result = lado_y_tan(a , b, c, d)
            plt.title("Período: " + str(result[2]))
            x = result[0]
            y= result[1]
            y = a+b*np.tan(c*x+d)
           
            plotar(x, y)
        elif op == "4":
            a = eval(input("Digite a: "))
            b = eval(input("Digite b: "))
            c = eval(input("Digite C: "))
            d = eval(input("Digite d: "))
        elif op == "5":
            i = 1
        else:
            print("Opção invalida")