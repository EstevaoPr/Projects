#P2 Q3
import math as mt
#Criando uma classe para tratar de matrizes
class Matrix :
    def __init__(self, n, e) :
        self.n = n
        #formando a matriz
        self.e = []
        for i in range(n) :
            a = []
            for j in range(len(e[0])) :
                a.append(e[i][j])
            self.e.append(a)
        return
    def __str__(self) :
        a = ""
        b = []
        for i in range(self.n) :
            for j in range(len(self.e[0])) :
                a = a + "\t" + str(self.e[i][j])
            a = a+"\n"
        return a
    def order (self) :
        x = 0
        b = 0
        for i in range(self.n) :
            x = i
            if self.e[i][i] == 0 :
                while self.e[x][i] == 0 :
                    if x == self.n - 1 :
                        break
                    x += 1
                    if self.e[x][i] != 0 :
                        for n in range(self.n + 1) :
                            b = self.e[i][n]
                            self.e[i][n] = self.e[x][n]
                            self.e[x][n] = b
                        break
        return

def isolate_xs (m_a, m_b) :
    eq_f = []
    for i in range(len(m_a.e)):
        eq = []
        for j in range(len(m_a.e[0])):
            if i != j:
                eq.append(-1 * m_a.e[i][j])
        eq.append(m_b.e[i][0])
        for j in range(len(eq)):
            eq[j] /= m_a.e[i][i]
        eq_f.append(eq)
    return Matrix(len(eq_f), eq_f)

def print_Eq (Eq) :
    result = ""
    for i, k in enumerate(Eq.e) :
        a = 0
        for j, n in enumerate(k) :
            a += 1
            if j < len(k) - 1 :
                if j == i :
                    a += 1
                result += f"\t{k[j]}x{a}"
            else:
                result += f"\t{k[j]}"
        result += "\n"
    return result

def gauss_seidel (Eq, error,  x0 = Matrix(2, [[0], [0]]), k = 0) :
    k += 1
    if  k > 1 / error :
        return "O método não converge para o sistema informado"
    print(f"Solução inicial:\n{x0}")
    x1 = []
    for i in range(len(Eq.e)) :
        x1.append([])
    for i in range(len(Eq.e)) :
        a = 0
        b = []
        for j in range(len(Eq.e[0]) - 1) :
            if j == i :
                a += 1
            b.append(Eq.e[i][j] * x0.e[a][0])
        b.append(Eq.e[i][-1])
        x1[i].append(sum(b))
    x = Matrix(len(x1), x1)
    input(f"Resultado atual do metodo: \n{x}")
    diff = []
    for i in range(len(x.e)) :
        diff.append(mt.fabs(x.e[i][0] - x0.e[i][0]))
    if max(diff) > error :
        return gauss_seidel (Eq, error, x, k)
    else :
        return x

n = int(input("Quantas incógnitas há no sistema?\n\t"))
mat = []
a = 0
for i in range(n) :
    l1 = []
    for j in range(n+1) :
        if j == n :
            l1.append(float(input(f"Na equação {i+1}, qual o resultado da equação?\n\t")))
            continue
        l1.append(float(input(f"Na equação {i+1}, qual a constante que acompanha a incógnita x{j+1}?\n\t")))
        pass
    mat.append(l1)
    pass
m = Matrix(n, mat)

m.order()
print(f"A matriz extendida do sistema é:\n{m}")
A1 = []
for i in range(len(m.e)) :
    linha = []
    for j in range(len(m.e[0]) - 1) :
        linha.append(m.e[i][j])
    A1.append(linha)
B1 = []
for i in range(len(m.e)) :
    B1.append([])
for i in range(len(m.e)) :
    B1[i].append(m.e[i][-1])
A = Matrix(n, A1)
B = Matrix(len(B1), B1)
print(f"A: \n{A}\nB:\n{B}")
Eq = isolate_xs (A, B)
print(f"As equações utilizadas para calcular o valor da solução são:\n{print_Eq(Eq)}")
x_0 = []
for i in range(n) :
    x_0.append([])
for i in range(n) :
    x_0[i].append(float(input(f"Qual a solução inicial para x{i}\t")))
x0 = Matrix(n, x_0)
error = float(input("Qual o erro desejado? [Exemplo: 1e-2 = 10 ^-2]\n"))
resultado = gauss_seidel(Eq, error, x0)
print("A solução encontrada pelo método de Gauss-Seidel é:\n", resultado)
