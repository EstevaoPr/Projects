#Atividade método de Gauss
class Matrix :
    def __init__(self, n, e) :
        self.n = n
        #formando a matriz
        self.e = []
        for i in range(n) :
            a = []
            for j in range(n + 1) :
                a.append(e[i][j])
            self.e.append(a)
        return
    def __str__(self) :
        a = ""
        b = []
        for i in range(self.n) :
            for j in range(self.n + 1) :
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
        return

    def resultados (self) :
        a = self.gauss()
        if a == "error" :
            return "Não há solução"
        x = []
        a = "\tIncógnitas\tResultados\n"
        for i in range (self.n) :
            x.append(self.e[i][self.n])
        for m, n in enumerate(x) :
            a += f"\t\tx{m+1}\t\t{n}\n"
        return a
    
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
print("A matriz extendida para a resolução do sistema linear pelo método de elminação de Gauss é:\n", m)
input("\nPressione qualquer tecla\n")
print("A solução do sistema é dado por: \n", m.resultados())
input()
