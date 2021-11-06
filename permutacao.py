from cifracesar import caracter
chave = [2, 0, 3, 1, 4]
    
    #Cifrar dados
def criptografar_permuta(texto):
    fragmentos = []
    permuta = []
    n_texto = ""
    x = []
        #separa em fragmentos de até 4 carcteres (exc: o primeiro sera 5)
    for i in range(len(texto)):
        if i%4!=0.0 or i==0:
            x.append(texto[i])
        else:
            x.append(texto[i])
            fragmentos.append(x)
            x = []
    fragmentos.append(x)
    for i in fragmentos:
        if len(i)<4:
            for c in i:
                permuta.append(c)
        else:
            for g in range(len(i)):
                try:
                    permuta.append(i[chave[g]])
                except:
                        permuta.append(i[g])
        #embaralha os carcateres
    for i in permuta:
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
        x = caracter.index(i)+len(permuta)
        y = len(caracter)-x
        if y>0:
            n_texto = n_texto + caracter[x]
        else:
            n_texto = n_texto + caracter[-(y)]
    return n_texto
    
    #metodo para decifrar os dados
def decriptografar_permuta(texto):
    revert = []
    permuta = []
    fragmentos = []
    x = []
    letras = []
    reverter = n_texto = ""
        #decifrar Cesar para a permutacao
    for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
        x = caracter.index(texto[i])-len(texto)
        if x>=0:
            n_texto = n_texto + caracter[x]
        else:
            n_texto = n_texto + caracter[len(caracter)+x]

        #separa em fragmentos de ate 4 caracteres (exc: o primeiro sera 5)
    for i in range(len(n_texto)):
        if i%4!=0.0 or i==0:
            letras.append(n_texto[i])
        else:
            letras.append(n_texto[i])
            fragmentos.append(letras)
            letras = []
    fragmentos.append(letras)
        #desfazer a permutacao
    for i in fragmentos:
        if len(i)<4:
            for c in i:
                reverter = reverter+c
        else:
            for g in range(len(i)):
                try:
                    reverter = reverter+i[chave.index(g)]
                except:
                    reverter = reverter+i[g]
        permuta.append(reverter)
        reverter = ""
    for i in permuta:
        reverter = reverter+i
    
    return reverter