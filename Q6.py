
#Q6 P2
import matplotlib.pyplot as plt
import numpy as np

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
            a += f"\ta{m}\t\t{n}\n"
        return a
    pass

choice = -1
while (choice != 0) :
    choice = int(input("\n::::\t::::\tMENU\t::::\t::::\n1 - Questão 6 letra A\n2 - Questão 6 letra B\n3 - Questão 6 letra C\n0 - Encerrar programa...\n::::\t::::\t::::\t::::\t::::\n"))
    if (choice > 0 and choice < 4) :
        x = [-8, -6, -4, -2, 0, 2, 4]
        y = [30, 10, 9, 6, 5, 4, 4]
        a = "\nX\tY\n"
        for i in range(len(x)) :
            a += f"{x[i]}\t{y[i]}\n"
        print(a)
    if choice == 1 :
        print("\nPara ajustar a reta precisamos dos valores tabelados da função 1 / y")
        Y = [1 / i for i in y]
        a  = "\nX\tY\t1/Y\n"
        for i in range(len(Y)) :
            a += "{}\t{}\t{:.3f}\n".format(x[i], y[i], Y[i])
        print(a)
        input("tabelando as funções:\ng0(x) = 1\ng1(x) = x\ng0(x)^2 = 1\ng1(x)^2 = x^2\ng0(x) * g1(x) = x\n1/y * g0(x) = 1 / y\n1/y * g1(x) = x / y\n")
        G0, G1 = [1 for i in range(len(x))], [i for i in x]
        G0_2, G1_2 = [1 for i in range(len(x))], [i ** 2 for i in x]
        G0_G1 = [G0[i] * G1[i] for i in range(len(G0))]
        Y_G0, Y_G1 = [i for i in Y], [Y[i] * G1[i] for i in range(len(Y))]
        a  = "\nX\tY\t1/Y\tG0\tG1\tG0**2\tG1**2\tG0 * G1\t\t1/Y * G0\t\t1/Y * G1\n"
        for i in range(len(Y)) :
            a += "{}\t{}\t{:.3f}\t{}\t{}\t{}\t{}\t{}\t\t{:.3f}\t\t{:.3f}\n".format(x[i], y[i], Y[i], G0[i], G1[i], G0_2[i], G1_2[i], G0_G1[i], Y_G0[i], Y_G1[i])
        print(a)
        a0_1, a1_1, b0 = sum(G0_2), sum(G0_G1), sum(Y_G0)
        a0_2, a1_2, b1 = sum(G0_G1), sum(G1_2), sum(Y_G1)
        print(f"Realizando os somatórios de algumas colunas da tabela obtemos os seguintes valores:\nsomatório de g0(x)^2 = {a0_1:.3f} = sg0\nsomatório de g1(x)^2 =  {a1_2:.3f} = sg1\nsomatório de g0(x) * g1(x) = {a0_2:.3f} = g0g1\nsomatório de 1 / y * g0(x) = {b0:.3f} = fg0\nsomatório de 1 / y * g1(x) = {b1:.3f} = fg1")
        print(f"\nSendo assim, podemos calcular o valor de a0 e a1 pelo seguinte sistema:\n\ta0 * sg0 + a1 * g0g1 = fg0\n\ta0 * g0g1 + a1 * sg1 = fg1\n")
        M1 = [[a0_1, a1_1, b0], [a0_2, a1_2, b1]]
        M = Matrix(len(M1), M1)
        input(f"\nFormulando o sistema acima como uma equação matricial de A * X = B, onde\n   \tA\t\tX\t\tB\n[sg0\g0g1]\t\t[a0]\t\t[fg0]\n[g0g1\sg1]\t\t[a1]\t\t[fg1]\nSe realizarmos a matriz extendida de A com B, obtemos:\n{M}")
        X = M.gauss_jordan()
        print(f"\nA solução do sistema acima é dado por:\n{X.resultados()}")
        P1 = np.vectorize(lambda x : X.e[0][0] + X.e[1][0] * x)
        P = np.vectorize(lambda x : 1 / (X.e[0][0] + X.e[1][0] * x))
        print(f"\nDesta forma, a função que se aproxima dos pontos (x , 1 / y) é dada por P1(x) = {X.e[0][0]} + {X.e[1][0]} * x")
        input(f"\nPara determinarmos a função que se aproxima dos valore y, utilizaremos a função 1 / P(x) = 1 / ({X.e[0][0]} + {X.e[1][0]} * x)")
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(x, P1(x), label = f"P1(x) = {X.e[0][0]:.3f} + {X.e[1][0]:.3f} * x")
        ax1.plot(x, Y, "o-", label = "1 / y tabelado")
        ax1.legend();
        ax2.plot(x, P(x), label = f"P(x) = 1 / ({X.e[0][0]:.3f} + {X.e[1][0]:.3f} * x)")
        ax2.plot(x, y, "o-", label = "y tabelado")
        ax2.legend();
        plt.show()
    elif choice == 2 :
        print("\nPara ajustar a reta precisamos dos valores tabelados da função ln(y)")
        Y = [np.log(i) for i in y]
        a  = "\nX\tY\tln(Y)\n"
        for i in range(len(Y)) :
            a += "{}\t{}\t{:.3f}\n".format(x[i], y[i], Y[i])
        print(a)
        input("tabelando as funções:\ng0(x) = 1\ng1(x) = x\ng0(x)^2 = 1\ng1(x)^2 = x^2\ng0(x) * g1(x) = x\n1/y * g0(x) = 1 / y\n1/y * g1(x) = x / y\n")
        G0, G1 = [1 for i in range(len(x))], [i for i in x]
        G0_2, G1_2 = [1 for i in range(len(x))], [i ** 2 for i in x]
        G0_G1 = [G0[i] * G1[i] for i in range(len(G0))]
        Y_G0, Y_G1 = [i for i in Y], [Y[i] * G1[i] for i in range(len(Y))]
        a  = "\nX\tY\t1/Y\tG0\tG1\tG0**2\tG1**2\tG0 * G1\t\t1/Y * G0\t\t1/Y * G1\n"
        for i in range(len(Y)) :
            a += "{}\t{}\t{:.3f}\t{}\t{}\t{}\t{}\t{}\t\t{:.3f}\t\t{:.3f}\n".format(x[i], y[i], Y[i], G0[i], G1[i], G0_2[i], G1_2[i], G0_G1[i], Y_G0[i], Y_G1[i])
        print(a)
        a0_1, a1_1, b0 = sum(G0_2), sum(G0_G1), sum(Y_G0)
        a0_2, a1_2, b1 = sum(G0_G1), sum(G1_2), sum(Y_G1)
        print(f"Realizando os somatórios de algumas colunas da tabela obtemos os seguintes valores:\nsomatório de g0(x)^2 = {a0_1:.3f} = sg0\nsomatório de g1(x)^2 =  {a1_2:.3f} = sg1\nsomatório de g0(x) * g1(x) = {a0_2:.3f} = g0g1\nsomatório de 1 / y * g0(x) = {b0:.3f} = fg0\nsomatório de 1 / y * g1(x) = {b1:.3f} = fg1")
        print(f"\nSendo assim, podemos calcular o valor de a0 e a1 pelo seguinte sistema:\n\ta0' * sg0 + a1 * g0g1 = fg0\n\ta0' * g0g1 + a1 * sg1 = fg1\n")
        M1 = [[a0_1, a1_1, b0], [a0_2, a1_2, b1]]
        M = Matrix(len(M1), M1)
        input(f"\nFormulando o sistema acima como uma equação matricial de A * X = B, onde\n   \tA\t\tX\t\tB\n[sg0\g0g1]\t\t[a0]\t\t[fg0]\n[g0g1\sg1]\t\t[a1]\t\t[fg1]\nSe realizarmos a matriz extendida de A com B, obtemos:\n{M}")
        X = M.gauss_jordan()
        print(f"\nA solução do sistema acima é dado por:\n{X.resultados()}")
        print("a0' = ",X.e[0][0])
        a0 = np.exp(X.e[0][0])
        X.e[0][0] = a0
        print(f"\na0' = ln(a0), deste modo, temos que a0 = e^(a0') = {X.e[0][0]}")
        P = np.vectorize(lambda x : X.e[0][0] * np.exp(X.e[1][0] * x))
        P1 = np.vectorize(lambda x : np.log(X.e[0][0]) + X.e[1][0] * x)
        print(f"\nDesta forma, a função que se aproxima dos pontos (x , 1 / y) é dada por P1(x) = {X.e[0][0]} + {X.e[1][0]} * x")
        input(f"\nPara determinarmos a função que se aproxima dos valore y, utilizaremos a função P(x) = ({X.e[0][0]} + e**{X.e[1][0]} * x)")
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(x, P1(x), label = f"P1(x) = {np.log(X.e[0][0]):.3f} + x * {X.e[1][0]:.3f}")
        ax1.plot(x, Y, "o-", label = "ln(y) tabelado")
        ax1.legend();
        ax2.plot(x, P(x), label = f"P(x) = {X.e[0][0]:.3f} * e**({X.e[1][0]:.3f} * x)")
        ax2.plot(x, y, "o-", label = "y tabelado")
        ax2.legend();
        plt.show()
    elif choice == 3 :
        a0_a = 0.19583333333333333
        a1_a = 0.0185515873015873
        a0_b = 5.5199044545965
        a1_b = -0.15116209268352188
        Pa = lambda x : 1 / (a0_a + a1_a * x)
        Pb = lambda x : a0_b * np.exp(a1_b * x)
        Ra = []
        Rb = []
        Ra1 = []
        Rb1 = []
        for i in range(len(x)) :
            Ra.append((Pa(x[i]) - y[i]))
            Rb.append((Pb(x[i]) - y[i]))
            Ra1.append(Ra[i] ** 2)
            Rb1.append(Rb[i] ** 2)
        A, B = sum(Ra1), sum(Rb1)
        print("Para sabermos qual curva se ajustou melhor aos pontos tabelados, devemos analisar a distância entre os pontos e a função")
        print(f"Sabendo que Pa(x) = 1 / ({a0_a:.3f} + {a1_a:.3f} * x) e Pb(x) = {a0_b:.3f} * e ** ({a1_b:.3f} * x)")
        print(f"Deste modo, ao calcularmos a função Ra(x) = Pa(x) - y(x) e Rb(x) = Pb(x) - y(x), obtemos :")
        a = "\nX\tY\tRa\tRb\t\tRa ** 2\t\tRb ** 2\n"
        for i in range(len(x)) :
            a += f"{x[i]}\t{y[i]}\t{Ra[i]:.3f}\t{Rb[i]:.3f}\t\t{Ra1[i]:.3f}\t\t{Rb1[i]:.3f}\n"
        print(a)
        print(f"\nAo realizar os somatórios das colunas Ra ** 2 e Rb ** 2, obtemos:\nResíduo total a = {A}\nResíduo total b = {B}")
        if A < B :
            input(f"\nComo o resíduo da curva Pa(x) = 1 / ({a0_a:.3f} + {a1_a:.3f} * x)  é inferior ao da curva Pb(x) = {a0_b:.3f} * e ** ({a1_b:.3f} * x)\nentendemos que a curva Pa(x) é um melhor ajustamento de curva")
        if A > B :
            input(f"\nComo o resíduo da curva Pb(x) = {a0_b:.3f} * e ** ({a1_b:.3f} * x) é inferior ao da curva Pa(x) = 1 / ({a0_a:.3f} + {a1_a:.3f} * x)\nentendemos que a curva Pb(x) é um melhor ajustamento de curva")
