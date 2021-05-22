import math

def conversor_graus(angulo_a, angulo_b, angulo_c):
    angulo_a = math.degrees(angulo_a) 
    angulo_b = math.degrees(angulo_b)
    angulo_c = math.degrees(angulo_c)
    return (angulo_a, angulo_b, angulo_c)

def conversor_radianos(angulo_a, angulo_b, angulo_c):
    angulo_a = math.radians(angulo_a)
    angulo_b = math.radians(angulo_b)
    angulo_c = math.radians(angulo_c)
    return (angulo_a, angulo_b, angulo_c)
    
def calculo_area(lado_a, lado_b, angulo_c):
    angulo_c = math.radians(angulo_c) 
    angulo_c = math.sin(angulo_c)
    area = (lado_a * lado_b * angulo_c)/ 2
    return area 

def bascara(a,b,c):
    delta = b**2  - 4*a*c
    raiz = (delta) ** (1/2)
    if delta >= 0:
        x = (-b - raiz) / 2
        return -x
    return False

def lei_cossenos(lado_oposto,lado1,lado2,angulo):
    if  lado_oposto == 0 and lado1 !=0 and lado2 != 0 and angulo != 0:
        angulo = math.radians(angulo)
        cos = math.cos(angulo)
        result = (lado1 ** 2 + lado2 ** 2 - 2 * lado1 * lado2 * cos) ** (1/2)
        return result
    elif lado1 == 0 and lado_oposto != 0 and angulo != 0 and lado2 != 0:
        angulo = math.radians(angulo)
        cos = math.cos(angulo)
        b = lado2 * 2 * cos
        c = lado2 ** 2 - (lado_oposto ** 2)
        a = 1
        return bascara(a, b, c)
    elif angulo == 0 and lado1 != 0 and lado2 != 0 and lado_oposto != 0:
        cos = lado1 * lado2 * 2
        valor = -(lado_oposto ** 2) + lado1 ** 2 + lado2 ** 2
        result = valor/cos
        result = math.acos(result)
        result = math.degrees(result)
        return result                                                                                      
    return False

def lei_dos_senos(angulo, angulo_oposto, lado, lado_oposto):
    if lado_oposto == 0 and (angulo_oposto != 0 and lado != 0 and angulo != 0):
        sen_angulo = math.radians(angulo)
        sen_angulo=math.sin(sen_angulo)
        sen_angulo_oposto = math.radians(angulo_oposto)
        sen_angulo_oposto=math.sin(sen_angulo_oposto)
        result = sen_angulo_oposto * lado / sen_angulo
        return result
    return False

'''
Pega os valores e chama outras funções de acordo com os valores que foram dados
'''
def main(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c, opcao):
    if opcao == "2":
        graus = conversor_graus(angulo_a, angulo_b, angulo_c)
        angulo_a = graus[0]
        angulo_b = graus[1]
        angulo_c = graus[2]

    if ((lado_a != 0 and lado_b != 0) or (lado_a != 0 and lado_c != 0) or (lado_b != 0 and lado_c != 0) or (lado_a != 0 and lado_b != 0 and lado_c != 0)) and (angulo_a == 0 or angulo_b == 0 or angulo_c == 0):
        if lado_a != 0 and lado_b != 0:
            if angulo_a != 0:    
                lado_c = lei_cossenos(lado_a, lado_c, lado_b, angulo_a)
            elif angulo_b != 0:
                lado_c = lei_cossenos(lado_b, lado_c, lado_a, angulo_b)
            elif angulo_c != 0:
                lado_c = lei_cossenos(lado_c, lado_a, lado_b, angulo_c)
        elif lado_a != 0 and lado_c != 0:
            if angulo_a != 0:
                lado_b = lei_cossenos(lado_a, lado_b, lado_c, angulo_a)
            elif angulo_b != 0:
                lado_b = lei_cossenos(lado_b, lado_c, lado_a, angulo_b)
            elif angulo_c != 0:
                lado_b = lei_cossenos(lado_c, lado_b, lado_a, angulo_c)
        elif lado_b != 0 and lado_c != 0:
            if angulo_a != 0:
                lado_a = lei_cossenos(lado_a, lado_b, lado_c, angulo_a)
            elif angulo_b != 0:
                lado_a = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
            elif angulo_c != 0:
                lado_a = lei_cossenos(lado_c, lado_a, lado_b, angulo_c)
        angulo_a, angulo_b, angulo_c = 0, 0, 0
        angulo_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
        angulo_c = lei_cossenos(lado_c, lado_a, lado_b, angulo_c)
        angulo_a = lei_cossenos(lado_a, lado_c, lado_b, angulo_a)
    elif ((angulo_a != 0 and angulo_b != 0) or (angulo_a != 0 and angulo_c != 0) or (angulo_c != 0 and angulo_b != 0)) and (lado_a == 0 or lado_b == 0 or lado_c == 0):
        if angulo_a != 0 and angulo_b != 0:
            angulo_c = 180 - angulo_a - angulo_b
            if lado_a != 0:
                lado_b = lei_dos_senos(angulo_a, angulo_b, lado_a, lado_b)
                lado_c = lei_cossenos(lado_c, lado_a, lado_b, angulo_c)  
            elif lado_b != 0:
                lado_a = lei_dos_senos(angulo_b, angulo_a, lado_b, lado_a)
                lado_c = lei_cossenos(lado_b, lado_c, lado_a, angulo_b)
            elif lado_c != 0:
                lado_a = lei_dos_senos(angulo_c, angulo_a, lado_c, lado_a)
                lado_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
        elif angulo_a != 0 and angulo_c != 0:
            angulo_b = 180 - angulo_a - angulo_c
            if lado_a != 0:
                lado_c = lei_dos_senos(angulo_a, angulo_c, lado_a, lado_c)
                lado_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
            elif lado_b != 0:
                lado_a = lei_dos_senos(angulo_b, angulo_a, lado_b, lado_a)
                lado_c = lei_cossenos(lado_c, lado_b, lado_a, angulo_c) 
            elif lado_c != 0:
                lado_a = lei_dos_senos(angulo_b, angulo_a, lado_b, lado_a)
                lado_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
        elif angulo_c != 0 and angulo_b != 0:
            angulo_a = 180 - angulo_b - angulo_c
            if lado_a != 0:
                lado_c = lei_dos_senos(angulo_a, angulo_c, lado_a, lado_c)
                lado_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b)
            elif lado_b != 0:
                lado_a = lei_dos_senos(angulo_b, angulo_a, lado_b, lado_a)
                lado_c = lei_cossenos(lado_c, lado_a, lado_b, angulo_c)
            elif lado_c != 0:
                lado_a = lei_dos_senos(angulo_c, angulo_a, lado_c, lado_a)
                lado_b = lei_cossenos(lado_b, lado_a, lado_c, angulo_b) 
    else:
        print("=====================")
        print("|  Opções Iválidas  |")
        print("=====================")
        return interface()
    area = calculo_area(lado_a, lado_b, angulo_c)
    return (lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c, area) 

def interface():
    while True:
        print("==================")
        opcao = input("Você deseja informar em graus(1) ou em radianos(2):")
        lado_a = float(input("Lado a: "))
        lado_b = float(input("Labo b: "))
        lado_c = float(input("lado c: "))
        angulo_a = float(input("Angulo A: "))
        angulo_b = float(input("Angulo B: "))
        angulo_c = float(input("Angulo C: "))
        result = main(lado_a, lado_b, lado_c, angulo_a, angulo_b, angulo_c, opcao)
        print("\n================\nResultado:\n===============\n")
        print("Lado a = ", result[0])
        print("Lado b = ", result[1])
        print("Lado c = ", result[2])
        print("Angulo A = ", result[3], "graus")
        print("Angulo B = ", result[4], "graus")
        print("Angulo C = ", result[5], "graus")
        radianos = conversor_radianos(result[3], result[4], result[5])
        print("Angulo a = ", radianos[0], "radianos")
        print("Angulo b = ", radianos[1], "radianos")
        print("Angulo c = ", radianos[2], "radianos")
        print("area = ", result[6])
        print("")
        print("==================")
        print("")
interface()