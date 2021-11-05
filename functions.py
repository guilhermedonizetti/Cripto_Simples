caracter = [
            'A','B','C','D','E','Ô','F','G','H','I','J','K','L',
            'N','f','g','h','í','O','Q','W','X','Y','Z','6','7',
            ' ','a','b','c','d','e','+','i','j','k','l','8','9',
            'm','n','o','p','q','r','s','t','u','v','w','x','y',
            'z','1','2','Ç','3','4','5','R','S','T','U','V','\n',
            '?','!',':','$','-','/','*','%','(',')','Ã','Â','À',
            'Á','É','Ê','Í','M','Ó','Õ','Ú','á','â','à','ã','é',
            'ê','ó','õ','ô','0','.','ç',',','ú','@','P',';'
        ]
    
#Transforma o texto puro em um texto criptografado
def criptografar_cesar(texto, chave):
    #se o tamanho da chave for maior que o texto
    if len(chave)>len(caracter):
        return False
    else:
        nvtexto = "" 
        for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])+len(chave)
            y = len(caracter)-x
            if y>0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[-(y)]
            
        return nvtexto

#Reverte a criptografia para o texto puro
def decriptografar_cesar(texto, chave):
    if len(chave)>len(caracter):
        return False
    else:
        nvtexto = ""
        for i in range(len(texto)):
            # x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])-len(chave)
            if x>=0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[len(caracter)+x]
        
        return nvtexto