import matplotlib.pyplot as plt

def main():
    x = eval(input("Digite x: "))
    y = eval(input("Digite y: "))
    while True:
        valores = input("Deseja altear os valores(s/n): ")
        if valores == "s": 
            x = eval(input("Digite x: "))
            y = eval(input("Digite y: "))
        list(x)
        list(y)
        print("1.\n2.\n3.")
        print("4.Parar o programa")
        op = input("Digite a opção: ")
        cordenadas_x = [x]
        cordenadas_y = [y]
        if op == '1':
            cordenadas = q1(cordenadas_x, cordenadas_y)
            cordenadas_x = cordenadas[0]
            cordenadas_y = cordenadas[1]
            for i in range(16):
                plt.fill(cordenadas_x[i], cordenadas_y[i])
            plt.show()

        elif op == '2':
            cordenadas = q2(cordenadas_x, cordenadas_y)
            cordenadas_x = cordenadas[0]
            cordenadas_y = cordenadas[1]
            for i in range(16):
                plt.fill(cordenadas_x[i], cordenadas_y[i])
            plt.show()

        elif op == '3':
            cordenadas = q3(cordenadas_x, cordenadas_y)
            cordenadas_x = cordenadas[0]
            cordenadas_y = cordenadas[1]
            for i in range(16):
                plt.fill(cordenadas_x[i], cordenadas_y[i])
            plt.show()
        elif op == '4':
            break
        
        else:
            print("\n")
            print("Opção invalida!!!!!\n")
            
def mover(xy, casa=1):
    num = max(xy) - min(xy)
    result = []
    if num < 0:
        num = num * (-1)    
    for i in range(len(xy)):
        result.append(num * casa + xy[i])
    return result

def espelhar(xy):
    result = []    
    for i in range(len(xy)):
        result.append((-1) * xy[i])
    return result

def q1(cordenadas_x, cordenadas_y):
    cordenadas_x.append(mover(cordenadas_x[0]))
    cordenadas_y.append(cordenadas_y[0])
    for i in range(2):    
        cordenadas_y.append(mover(cordenadas_y[i]))
        cordenadas_x.append(cordenadas_x[i])
    c = mover_4(cordenadas_x, cordenadas_y)
    cordenadas_x = c[0]
    cordenadas_y = c[1]
    t = "x = " + str(cordenadas_x[15]) + "\n y = " + str(cordenadas_y[15])
    print(" 4 x 4\n",t)
    return(cordenadas_x, cordenadas_y)


def q2(cordenadas_x, cordenadas_y):   
    valor = espelhar(cordenadas_x[0])
    cordenadas_x.append(mover(valor, 2))
    cordenadas_y.append(cordenadas_y[0])
    for i in range(2):
        valor = espelhar(cordenadas_y[i])
        cordenadas_y.append(mover(valor, 2))
        cordenadas_x.append(cordenadas_x[i])
    cord = mover_4(cordenadas_x, cordenadas_y)
    cordenadas_x = cord[0]
    cordenadas_y = cord[1]
    t = "3 x 3\nx = " + str(cordenadas_x[12]) + "\ny = " + str(cordenadas_y[12])
    t = t + "\n" +"3 x 4\nx = " + str(cordenadas_x[13]) + "\ny = " + str(cordenadas_y[13])
    t = t + "\n" +"4 x 3\nx = " + str(cordenadas_x[14]) + "\ny = " + str(cordenadas_y[14])
    t = t + "\n" +"4 x 4\nx = " + str(cordenadas_x[15]) + "\ny = " + str(cordenadas_y[15])
    print(t)
    return (cordenadas_x, cordenadas_y)
    
def q3(cordenadas_x, cordenadas_y):
    v1 = espelhar(cordenadas_y[0])
    v2 = cordenadas_y[0]
    cordenadas_y[0] = mover(v1, 2)
    v3 = espelhar(cordenadas_x[0])
    cordenadas_x.append(mover(v3))
    cordenadas_y.append(v2)
    cordenadas_x.append(mover(cordenadas_x[1]))
    cordenadas_y.append(mover(cordenadas_y[1]))
    cordenadas_x.append(mover(cordenadas_x[0]))
    cordenadas_y.append(mover(cordenadas_y[0],-1))
    c = mover_4(cordenadas_x, cordenadas_y)
    t = "3 x 3\nx = " + str(c[0][12]) + "\ny = " + str(c[1][12])
    t = t + "\n" +"3 x 4\nx = " + str(c[0][14]) + "\ny = " + str(c[1][14])
    print(t)
    return(c[0], c[1])

def mover_4(cordenadas_x, cordenadas_y):
    for i in range(4):
        if cordenadas_x[i] != 0:
            cordenadas_x.append(mover(cordenadas_x[i], 2))
            cordenadas_y.append(cordenadas_y[i])
    for i in range(8):
        if cordenadas_x[i] != 0:
            cordenadas_y.append(mover(cordenadas_y[i], 2))   
            cordenadas_x.append(cordenadas_x[i])
    return(cordenadas_x, cordenadas_y)

if __name__ == "__main__":
    main()
