#Prova 01
# importing required modules
import matplotlib.pyplot as plt
import numpy as np
import math

F = lambda x : np.exp(x) + x**2 #Função a calcular a área
def regra_trapezio(func, n = 1, interval = [0, 1], error = 5e-2) : #Regra dos traapézios repetidos
    x_max, x_min, I = interval[1], interval[0], 0
    h = (x_max - x_min) / n #Armazena a largura dos trapézios
    for i in range(n) :
        x0 = x_min + h * i
        xi = x0 + h
        I += (h / 2) * (func(x0) + func(xi)) #Calcula o valor da área de cada trapézio e acrescenta a variável I
    input(f"\nO valor calculado pela regra dos trapézios repetida foi:\t{I}\n...Utilizamos {n} trapézios para calcular...\n")
    if math.fabs((I - 2.051)) >= error : #Verifica se o erro é superior ao estabelecido
        return regra_trapezio(func, n + 1) #Caso for, chama a função com um trapézio a mais
    else :
        return I, n #Retorna o valor da área e a quantidade de trapézios utilizado
select = input("Pressione 1 para calcular a área da função exp(x) + x**2, no intervalo [0, 1], pelo método do trapézio\n")
if select == "1" :
    I, n = regra_trapezio(F)
    print(f"\nPela regra dos trapézios repetido, a área sob a curva f(x) = exp(x) + x**2 no intervalor [0, 1] é dada por: {I}")
input()

h = 1 / n

for i in range(n) : #Plota os trapézios
    x0 = 0 + h * i
    xi = x0 + h
    tx, ty = [x0, xi], [F(x0), F(xi)]
    plt.plot(tx, ty, color = "b", label = "trapézio", linewidth = 3.0)
    plt.plot([x0, x0], [0, F(x0)], color = "b", linewidth = 3.0)
    plt.plot([xi, xi], [0, F(xi)], color = "b", linewidth = 3.0)
x2 = np.arange(0, 1.3, 0.1) #x2 armazena um array com todos os números de 0 a 1.3 com 0.01 de espaço entre eles
y2 = np.vectorize(F)(x2) #y2 armazena um array com os valores de F(x2)
plt.plot(x2, y2, color ="r", label = "f(x) = exp(x) + x**2", linewidth = 2.0) #Plota a função F(x2)
plt.legend() #Exibe as legendas do gráfico
plt.show() #Exibe o gráfico
