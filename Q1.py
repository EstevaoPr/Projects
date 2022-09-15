
#Q1 P2
def dec_to_bin (num) :
    intg = int(num)
    deci = num - intg
    num1 = []
    number = []
    a = intg
    while (a > 1) :
        num1.append(a % 2)
        a = a // 2
        if a == 1 :
            num1.append(1)
    a = deci
    for i in range(1, len(num1) + 1) :
        number.append(num1[-1 * i])
    number.append(".")
    while (a != 0 or a >1e-2) :
        a *= 2
        number.append(int(a))
        a = a - int(a)
    b = ""
    for i in number :
        b += str(i)
    return float(b)

def bin_to_dec (num) :
    n = str(num)
    n1 = []
    j = 0
    while (n[j] != "." if len(n1) > 0 else True ) :
        n1.append(int(n[j]))
        j += 1
    n2 = []
    for l in range(j + 1, len(n)) :
        n2.append(int(n[l]))
    j = len(n1) - 1
    num1 = 0
    for l in n1 :
        if l == "." :
            continue
        num1 += l * 2 ** j
        j -= 1
    j = 1
    num2 = 0
    for l in n2 :
        num2 += l * (1 / 2) ** j
        j += 1
    number = int(num1) + (float(num2))
    return number

def floating_point (number, b = 2, t = 5, e1 = -7, e2 = 7) :
    n = str(number)
    M = []
    k, z, r = 0, 0, 0
    for i in range(len(n)) :
        if n[i] == "." and n[0] != "0":
            k = i - 1
            continue
        elif n[i] != "0" and n[i] != "." and n[0] == "0" and z == 0 :
            k = -i + 1
            z += 1
            M.append(n[i])
            continue
        if n[i] == "." :
            continue
        M.append(n[i])
    while (M[r] == "0") :
        M.pop(0)
    m = []
    for i in range(t) :
        if i == 1 :
            m.append("." + M[i])
        else :
            m.append(M[i])
    a = ""
    f = ""
    for i in m :
        a += i
        f += i
    a += " * " + str(b) + "**(" + str(k) + ")"
    nf = float(f) * 10 ** float(k)
    return a, nf

x = 0.3
n = dec_to_bin(x)
rn = floating_point(n)[-1]
nd = bin_to_dec(rn)
erro_a = x - nd
erro_r = erro_a / nd
choice = -1
while (choice != 0) :
    choice = int(input(":::\t:::\tMENU\t:::\t:::\n1 - Questão 1 letra A\n2 - Questão 1 letra B\n3 - Questão 1 letra C\n4 - Questão 1 letra D\n0 - Encerrar programa\n"))
    if choice == 1 :
        input(f"\n\tA representação binária de {x} = {n}")
    elif choice == 2 :
        input(f"\n\tEscrevendo o número {n} em ponto flutuante da máquina F(2, 5, -7, 7), obtemos:\n\t{ floating_point(n)[0]}\n")
    elif choice == 3 :
        input(f"\n\tConvertendo a representação truncada {rn} em decimal, obtemos:\n\t{nd}\n")
    elif choice == 4 :
        input(f"\n\tO erro absoluto do número representado na letra b e o número {x} é de: {erro_a}\n\tO erro relativo é dado por: {erro_r}\n")
        print(f"{x} - {nd} = {x - nd}")
    elif choice == 0 :
        continue
    else :
        input("\nEntrada inválida...")
