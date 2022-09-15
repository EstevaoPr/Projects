def run_langton(rules, size) :
    #Assegurando regras
    rules = rules.lower()
    
    #Definindo quadro
    quadro = []
    for i in range(size) :
        line = []
        for n in range(size) :
            line.append(0)
        quadro.append(line)

    #Posicionando formiga e iniciando contador
    x = size // 2
    y = size // 2
    count = 0
    
    #Direção
    dr = 0
    
    #definindo limite de cores conforme a regra
    limit = len(rules) - 1

    #Iniciando movimmentação
    while True :

        #Colorindo célula
        if quadro[y][x] == limit :
            quadro[y][x] = 0
        else :
            quadro[y][x] += 1

        #Movimentando formiga
        if  dr == 0 :
            y -= 1
        elif dr == 1 :
            x += 1
        elif dr == 2 :
            y += 1
        elif dr == 3 :
            x -= 1
        count += 1
        
        #Direcionando formiga
        #Verificando se a posição se encontra no quadro
        try :
            if rules[quadro[y][x]] == "r" :
                if dr == 3 :
                    dr = 0
                else :
                    dr += 1
            else :
                if dr == 0 :
                    dr = 3
                else :
                    dr -= 1
        except IndexError :
            return (count, quadro)
    pass
a = run_langton("RRL", 5)
print(a[0])
        
