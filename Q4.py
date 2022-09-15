    #P1 Q4
#Definindo uma classe para tratar de matrizes
import math as m
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
    def gauss_jordan (self) :
        self.order() #garante que o primeiro pivô não seja 0 e coloca a matriz em uma ordem mais conveniente
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
        print("A solução do sistema é dado pela matriz extendida: \n", self)
        x = []
        for i in range(len(self.e)) :
            x.append([self.e[i][-1]])
        return Matrix(len(x), x)

    def resultados (self) :
        x = []
        a = "\tIncógnitas\tResultados\n"
        for i in range (self.n) :
            x.append(self.e[i][-1])
        for m, n in enumerate(x) :
            a += f"\t\tx{m+1}\t\t{n}\n"
        return a
    pass
def newton_method (J_eq, F_eq, x0 = Matrix(2, [[0],[0]]), error = 1e-3, max_iteration = 3, k = 0) :
    y = k + 1
    print(f"\nA solução inicial x{k}: \n{x0}")
    x_0  = []
    for i in range(len(x0.e)) :
        x_0.append(x0.e[i][0])
    S_eq = []
    for i in range(len(J_eq.e)) :
        S_lin = []
        for j in range(len(J_eq.e[0]) + 1) :
            if j == len(J_eq.e[0]) :
                S_lin.append(F_eq.e[i][0](*x_0))
            else :
                S_lin.append(J_eq.e[i][j](*x_0))
        S_eq.append(S_lin)
    S = Matrix(len(S_eq), S_eq)
    print("\nA matriz extendida de J e F é dada por:\n", S)
    s = S.gauss_jordan()
    if type(s) == str :
        return f"\n\tErro, o sistema não possui solução..."
    x_ = []
    for i in range(len(s.e)) :
        x_.append([-s.e[i][0] + x0.e[i][0]])
    x = Matrix(len(x_), x_)
    diff = []
    for i in range(len(x.e)) :
        diff.append(m.fabs(x.e[i][0] - x0.e[i][0]))
    print("\nO erro atual calculado é de: ", max(diff))
    if max(diff) > error and k != max_iteration:
        return newton_method(J_eq, F_eq, x, k = y)
    return x, k

Fa_1 = lambda x1, x2 : 4 * x1**2 - 20 * x1 + x2**2 / 4 + 8
Fa_2 = lambda x1, x2 : x1 * x2**2 / 2 + 2 * x1 - 5 * x2 +8
Fa = Matrix(2, [[Fa_1], [Fa_2]])

Ja_11 = lambda x1, x2 : 8 * x1 - 20
Ja_12 = lambda x1, x2 : x2 / 2
Ja_21 = lambda x1, x2 : x2**2 / 2 + 2
Ja_22 = lambda x1, x2 : x1 * x2 - 5
Ja = Matrix(2, [[Ja_11, Ja_12], [Ja_21, Ja_22]])

Fb_1 = lambda x1, x2 : m.sin(4 * m.pi * x1 * x2) - 2 * x2 - x1
Fb_2 = lambda x1, x2 : (1 - 1 / (4 * m.pi)) * (m.exp(2 * x1) - m.e) + 4 * m.e * x2**2 - 2 * m.e * x1
Fb = Matrix(2, [[Fb_1], [Fb_2]])

Jb_11 = lambda x1, x2 : 4 * m.pi * x2 * m.cos(4 * m.pi * x1 * x2) - 1
Jb_12 = lambda x1, x2 : 4 * m.pi * x1 * m.cos(4 * m.pi * x1 * x2) - 2
Jb_21 = lambda x1, x2 : 2 * (1 - 1 / (4 * m.pi)) * m.exp(2 * x1) - 2 * m.e
Jb_22 = lambda x1, x2 : 8 * m.e * x2
Jb = Matrix(2, [[Jb_11, Jb_12], [Jb_21, Jb_22]])

Fc_1 = lambda x1, x2 : x1 * (1 - x1) + 4 * x2 - 12
Fc_2 = lambda x1, x2 : (x1 - 2)**2 + (2 * x2 - 3)**2 - 25
Fc = Matrix(2, [[Fc_1], [Fc_2]])

Jc_11 = lambda x1, x2 : 1 - 2 * x1
Jc_12 = lambda x1, x2 : 4
Jc_21 = lambda x1, x2 : 2 * x1 - 4
Jc_22 = lambda x1, x2 : 8 * x2 - 12
Jc = Matrix(2, [[Jc_11, Jc_12], [Jc_21, Jc_22]])

Fd_1 = lambda x1, x2 : 5 * x1**2 - x2**2
Fd_2 = lambda x1, x2 : x2 - 14 * (m.sin(x1) + m.cos(x2))
Fd = Matrix(2, [[Fb_1], [Fb_2]])

Jd_11 = lambda x1, x2 : 10 * x1
Jd_12 = lambda x1, x2 : -2 * x2
Jd_21 = lambda x1, x2 : -14 * m.cos(x1)
Jd_22 = lambda x1, x2 : 1 + 14 * m.sin(x2)
Jd = Matrix(2, [[Jd_11, Jd_12], [Jd_21, Jd_22]])

choice = -1
while choice != 0 :
    test = 0

    choice = int(input("\n\t::::\t:::\tMENU\t:::\t:::\n1 - Questão 4 letra A\n2 - Questão 4 letra B\n3 - Questão 4 letra C\n4 - Questão 4 letra D\n0 - Ecerrar programa\n\t:::\t:::\t\t:::\t:::\n"))
    if choice == 1 :
        print(f"O sistema não linear é dado por:\n\t4 * (x1)^2 - 20 * x1 + ((x2)^2) / 4 = -8\n\t(x1 * (x2)^2) / 2 + 2 * x1 - 5 * x2 = -8\n")
        x, k = newton_method(Ja, Fa)
        test += 1
        print(f"A solução para x{k}: \n{x.resultados()}")
    elif choice == 2 :
        print(f"O sistema não linear é dado por:\n\tsin(4 * pi * x1 * x2) - 2 * x2 - x1 = 0\n\t(1 - 1 / (4 * pi)) * (e^(2 * x1) - e) + 4 * e * x2^2 - 2 * e * x1 = 0\n")
        test += 1
        x, k = newton_method(Jb, Fb)
        print(f"A solução para x{k}: \n{x.resultados()}")
    elif choice == 3 :
        print(f"O sistema não linear é dado por:\n\tx1 * (1 - x1) + 4 * x2 = 12\n\t(x1 - 2)^2 + (2 * x2 - 3)^2 = 25\n")
        test += 1
        x, k = newton_method(Jc, Fc)
        print(f"A solução para x{k}: \n{x.resultados()}")
    elif choice == 4 :
        try :
            print(f"O sistema não linear é dado por:\n\t5 * (x1)^2 = (x2)^2\n\tx2 = 14 * (sin(x1) + cos(x2))\n")
            x, k = newton_method(Jd, Fd)
            print(f"A solução para x{k}: \n{x.resultados()}")
        except :
            print(newton_method(Jd, Fd))
    elif choice == 0 :
        input("Q4.py")
    else :
        print("Opção Inválida, escolha novamente...")
