#Atividades
import math as mt
class Vector :
    def __init__(self, coord) :
        self.coord = coord
        return
    def __str__(self) :
        vetor = ""
        for i in self.coord :
            vetor += "\t["+ str(i) + "]\n"
        return vetor
    def __mul__(self, other) :
        if isinstance(other, Vector) :
            result = []
            for i, n in enumerate(self.coord) :
                result.append(other.coord[i] * n)
            return Vector(result)
        if isinstance(other, int) or isinstance(other, float) :
            result = []
            for n in self.coord :
                result.append(other * n)
            return Vector(result)
    pass

class Matrix :
    def __init__(self, rows) :
        self.rows = rows
        return
    def row(self, n) :
        return self.rows[n]
    def col(self, n) :
        column = []
        for i in range(len(self.rows)) :
            column.append(self.rows[i][n])
        return column
    def add(self, other) :
        if isinstance(other, Matrix) :
            if len(self.rows) == len(other.rows) :
                rows = []
                lista = []
                for i in range(len(self.rows)) :
                    for n in range(len(self.rows[0])) :
                        lista.append(self.rows[i][n] + other.rows[i][n])
                    rows.append(lista)
                    lista = []
                result = Matrix(rows)
                return result
        return
    def mul(self, other) :
        if isinstance(other, Matrix) :
            if len(self.rows) == len(other.rows) :
                mat_res = []
                for i in range(len(self.rows)) :
                    mat_res.append([])
                    for j in range(len(other.rows[0])) :
                        result = [x*y for x,y in zip(self.row(i), other.col(j))]
                        mat_res[i].append(sum(result))
                resultado = Matrix(mat_res)
                return resultado
        elif isinstance(other, Vector) :
            if self.size()[1] == len(other.coord) :
                x = []
                for i in self.rows :
                    y = 0
                    for j, n in enumerate(other.coord) :
                        y += i[j] * n
                    x.append(y)
                return Vector(x)
        pass
    
    def __add__(self, other) :
        return self.add(other)
    def __mul__(self, other) :
        return self.mul(other)
    def __str__(self) :
        a = ""
        for i in range(len(self.rows)):
            a += "\t" + str(self.rows[i]) + "\n"
        return a
    pass

def round_num(num, digits) :
    cond = list(str(num))
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

def matriz_a (Sy) :
    A1 = []
    for i in range(len(Sy.rows)) :
        linha = []
        for j in range(len(Sy.rows)) :
            linha.append(Sy.rows[i][j])
        A1.append(linha)
    A = Matrix(A1)
    return A

def vetor_b (Sy) :
    b1 = []
    for i in range(len(Sy.rows)) :
        b1.append(Sy.rows[i][len(Sy.rows)])
    b = Vector(b1)
    return b

def Q25_a (matrix) :
    rows = len(matrix.rows)
    cols = len(matrix.rows[0])
    x = []
    b = []
    for i in range(rows) :
        x.append(0)
        b.append(0)
    for i in range(rows) :
        for n in range(cols - 1) :
            if mt.fabs(matrix.rows[i][n]) > x[i] :
                x[i] = int(mt.fabs(matrix.rows[i][n]))
                b[i] = n
            else:
                continue
    for i in range(len(x)) :
        for n in range(rows) :
            if n != i and x[i] == x[n] :
                return "Impossível"
    print("\nQuanto é x\n", x)
    for i in range(rows) :
        a = matrix.rows[i]
        matrix.rows[i] = matrix.rows[b[i]]
        matrix.rows[b[i]] = a
    return "É possível determinar se o método Jacobi é convergente, desde que o sistema se encontre na seguinte configuração:\n" + str(matrix)

def Q25_b (matrix, x0, e = 3) :
    A = matriz_a(matrix)
    print("A:\n",A)
    b = vetor_b(matrix)
    print("b:\n",b)
    x = []
    condition = True
    while condition :
        for i in range(len(x0.coord)) :
            soma = []
            for j in range(len(A.rows[0])) :
                if i == j :
                   continue
                else:
                    soma.append(A.rows[i][j] * x0.coord[j])
            x.append((b.coord[i] - sum(soma) ) / A.rows[i][i])
        x_f = Vector(x)
        for i in range(len(x_f.coord)) :
            condition = False if mt.fabs(x[i] - x0.coord[i]) < 10 ** -e else condition
        x0.coord = x
    return x_f

n = int(input("Informe quantas incógnitas há no sistema de equações:\t"))
system = []
for j in range(n) :
    linha = [float(input(f"\ninforme a constante que acompanha a incóginita x{i}:\t")) if i != n else float(input(f"\ninforme a solução da equação {j}:\t")) for i in range(n + 1)]
    system.append(linha)
Sy = Matrix(system)
print(f"O sistema:\n{Sy}")
select = -1
while select != 0 :
    select = int(input("\n\t\tMenu\n\t1 - Questão 25 letra a\n\t2 - Questão 25 letra b\n\t3 - Questão 28 letra a\n\t4 - Questão 28 letra b\n\t0 - Encerrar o programa!\n\t-_-_\t-_-_\t-_-_\n"))
    if select == 1 :
        print(Q25_a(Sy))
        input()
    elif select == 2 :
        x_0 = [float(input(f"\ndefina a solução inicial x0 --> x0[{i}] =\t")) for i in range(n)]
        x0 = Vector(x_0)
        e = int(input("Defina  a precisão (exemplo: 10 ** -2 --> digite 2)"))
        resultado = Q25_b(Sy, x0, e)
        print("a solução x encontrada é:\n", resultado)
        input()
