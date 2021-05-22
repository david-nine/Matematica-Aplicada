import numpy as np
import matplotlib.pyplot as plt

def cal_sistema(x, num):
    a = np.array([[x[0], 1], [x[1], 1]])
    b = np.array([num[0], num[1]])
    result = np.linalg.solve(a, b)
    return result

def grafico(result):
    cord_y = []
    x = np.arange(-50, 51, 1)
    for i in range(len(x)):
        y = result[0] * x[i] + result[1] 
        cord_y.append(y)
    plt.plot(x, cord_y)
    return(cord_y)

# a = [-2 ,18 ]
# b = [ 2, 12 ]
# c = [ 7, 3 ]
# d = [ 9,-1 ]

a = [ -12,-6 ]
b = [ -6,-2 ]
c = [ 10,5 ]
d = [ 25,15 ]

# a = [-12,10]
# b = [-6,6]
# c = [6,-2]
# d = [9,-4]

# a = [ , ]
# b = [ , ]
# c = [ , ]
# d = [ , ]

x1 = [a[0], b[0]]
x2 = [c[0], d[0]]
num1 = [a[1], b[1]]
num2 = [c[1], d[1]]
r1 = cal_sistema(x1, num1)
r2 = cal_sistema(x2, num2)
print('y =', r1)
print('y =', r2)
cy1 = grafico(r1)
cy2 = grafico(r2)
xf = [r1[0]*(-1), r2[0]*(-1)]
numf = [r1[1], r2[1]]
rf = cal_sistema(xf, numf)
if str(rf[0])[-3:-1] == '+1':
    print("S = { }")
    rf = 'SI'

elif cy1[0] == cy2[0]:
    print("x;",r1)
    rf = 'SPI'

else:
    print(rf)
    rf = "SPD"

print(rf)
plt.grid(True)
plt.show()