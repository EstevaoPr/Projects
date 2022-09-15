#P2 Q2
import math as m

#definido o radicando do qual desejamos descobrir a raiz
b = 3356

#definindo função F
F = lambda x : x**2 - b

#definido da derivada da função F: f
f = lambda x: 2*x

#definindo o método de Newton
def newton_method (x = 1, erro = 1e-4, x0 = -1, k = 0) :
    Dr = m.fabs(x - x0)
    while (Dr >= erro) :
        x0 = x
        print(f"x{k} = {x0}")
        print(f"F(x{k + 1}) = {F(x0)}\nf(x0) = {f(x0)}\nx = x{k} - F(x{k}) / f(x{k}) = {x0 - F(x0) / f(x0)}")
        input()
        x = x0 - F(x0) / f(x0)
        Dr = m.fabs(x - x0)
        k += 1
    return x, k
input("Calculo do valor da raíz quadrada de 3356 pelo método de newton!\n")
raiz, iteracao = newton_method()
input(f"O valor calculado pelo método de newton foi {raiz}\nFoi realizado {iteracao} iterações\nSe calcularmos x**(2) = {raiz**2}")
