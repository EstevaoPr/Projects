#Atividade 9 - Método_LU
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
        for i in range(len(self.e)) :
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

    def set_pivo(self, n) :
        #faremos o valor do pivô ir a 0
        if self.e[n][n] == 0 :
            print("O sistema não possui solução definida")
            return "error"
        elif self.e[n][n] == 1 :
            pass
        else :
            a = 1 / self.e[n][n]
            for i in range(n, self.n + 1) : #note que como os elementos na linha[n] antes da coluna [n] já estão em 0, não a necessidade de realizar iterações de 0 até self.n
                self.e[n][i] *= a
        return
           
    def triangular_inferior (self, n) :
        #utilizaremos o pivô de cada linha para zerar os demais elementos da mesma coluna nas linhas inferiores
        #self é a matriz extendida e n é o pivô que está sendo utilizado
        for i in range(n + 1, self.n):
            if self.e[n][n] == 0 :
                print("O sistema não possui solução definida")
                return "error"
            if self.e[i][n] != 0 :
                a = self.e[i][n] / self.e[n][n] #fator que multiplicará a linha do pivô utilizado para zerar a linha [i]
                for j in range(self.n + 1) :
                    self.e[i][j] -= self.e[n][j] * a #Subtrai da linha [i] a linha [n] multiplicada pelo fator a
        return

    def triangular_superior (self, n) :
        #utilizaremos o pivô de cada linha para zerar os demais elementos da mesma coluna nas linhas superiores
        #self é a matriz extendida e self.e[n][n] é o pivô qe está sendo utilizado
        if n == 0 :
            pass
        else :
            for i in range(n) :
                if self.e[n][n] == 0 :
                    print("O sistema não possui soluão definida")
                    return "error"
                elif self.e[i][n] != 0 :
                    a = self.e[i][n] / self.e[n][n]
                    for j in range(self.n + 1) :
                        self.e[i][j] -= self.e[n][j] * a                        
        return

    def gauss (self) :
        self.order() #garante que o primeiro pivô não seja 0 e coloca a matriz em uma ordem mais conveniente
        print(self)
        x = 0
        for i in range(self.n) :
           a = self.set_pivo(i)
           if a == "error" :
               return a
           a = self.triangular_inferior(i)
           if a == "error" :
               return a
        for j in range(self.n) :
           a = self.triangular_superior(j)
           if a == "error" :
               return a
        print("A matriz final gerada pelo método de eliminação de gauss é: \n", self)
        result = []
        for i in range(len(self.e)) :
            result.append([])
        for i in range(len(self.e)) :
            result[i].append(round_num(self.e[i][-1], 4))
        x = Matrix(len(result), result)
        print("A solução é:\n", x)
        return x
    
    def create_LU (self) :
        L = Matrix(0,0)
        U = Matrix(0,0)
        size = len(self.e)
        for i in range(size) :
            L.e.append([])
            U.e.append([])
            for j in range (size) :
                L.e[i].append(0)
                U.e[i].append(0)
        for m in range(size) :# colunas para L e linhas para U
            for n in range(size) :# linhas para L e colunas para U
                s1 = 0
                for a in range(m) :
                    s1 += L.e[n][a] * U.e[a][m]
                L.e[n][m] = self.e[n][m] - s1
            for n in range(size):
                s2 = 0
                if L.e[m][m] == 0 :
                    return "Imposível resolver o problema, há 0 na diagonal principal de L"
                for b in range(m) :
                    s2 += L.e[m][b] * U.e[b][n]
                t = self.e[m][n] - s2
                t /= L.e[m][m]
                U.e[m][n] = t
        return [L,U]
def metodo_LU(A, B) :
    mm = A.create_LU()
    L, U = mm[0], mm[1]
    L_e = Matrix(len(L.e), L.e)
    for i in range(len(B.e)) :
        L_e.e[i].append(B.e[i][0])
    print("Sistema L * Y = B\n", L_e)
    input()
    Y = L_e.gauss()
    U_e = Matrix(len(U.e), U.e)
    for i in range(len(Y.e)) :
        U_e.e[i].append(Y.e[i][0])
    print("Sistema U * X = Y\n", L_e)
    X = U_e.gauss()
    return X

def round_num(num, digits) :
    cond = list(str(num * 10 ** digits))
    index = cond.index(".")
    if int(cond[index + 1]) >= 5 :
        a = num * 10 ** digits
        a = int(a)
        a += 1
        b = a * 10 ** -digits
        return b
    else :
        a = num * 10 ** digits
        a = int(a)
        b = a * 10 ** -digits
        return b
    pass

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
print(m)
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
print(f"O sistema é solucionado pela equação\nA * X = B\nA =\n{A}\nB =\n{B}")
X = metodo_LU(A,B)
a = "\tIncógnitas\tResultados\n"
for m in range (X.n) :
    a += f"\t\tx{m+1}\t\t{X.e[m]}\n"
print(a)
input("Pressione 2 x enter para encerrar o programa")
input()
