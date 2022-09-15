#Q7 P2
import numpy as np
import matplotlib.pyplot as plt

func = lambda x : x**2 if (x <= 1) else (x + 2)**2
print("A função a ser integrada é definida como:\n")
print("f =\tx^2\t se 0 <= x <= 1\n\t(x + 2)^2\t se 1 < x <= 2")
print("\nComo o intervalo da integral é dado por [0, 2]\npodemos utilizar apenas três pontos para executar o método de Simpson")
print("\nOs pontos serão x0 = 0, x1 = 1 e x2 = 2")
X = [0,1,2]
Y = [func(i) for i in X]
E = []
P = []
I = []
h = ( X[1] - X[0] ) 
for i in range(len(X)) :
    if i ==0 or i == len(X) - 1 :
        E.append(Y[i])
    elif i % 2 :
        I.append(Y[i])
    else :
        P.append(Y[i])
a = f"({h} / {3}) * ("
for i in range(len(E)) :
    if i == len(E) :
        a += f"{i}) "
    else :
        a += f"{E[i]} + "
a += "+ 4 * (" if len(I) >= 1 else ""
for i in range(len(I)) :
    if i == len(I) - 1 :
        a += f"{I[i]})"
    else :
        a += f"{I[i]} + "
a += " + 2 * (" if len(P) >= 1 else ""
for i in range(len(P)) :
    if i == len(P) - 1 :
        a += f"{P[i]})"
    else :
        a += f"{P[i]} + "
a += ")"
b = "&f(x) = (h / 3) * (E + 4 * I + 2 * P)"
e = "E = termos extremos da função f(x) --> f(x0) e f(x n)"
i = "I = termos ímpares da função f(x) --> f(xi)"
p = "P = termos pares da função f(x) --> f(xp)"
H = "h = distancian entre xn e xn+1"
print("\nAssumindo que o termo & siginifica integral")
print("\nO método de Símpson afirma que:\n", b, "Onde :\n",e,"\n", i, "\n", p, "\n", H,"\n")
resultado = h / 3 * (sum(E) + 4 * sum(I) + 2 * sum(E))
input(f"O valor calculado pelo método de Simpson é\n{a} = {resultado}")
print("\nCom os pontos escolhidos a computação utilizada é mínima e a precisão é considerável devido ao uso de parábolas para determinar o cálculo da integral")
