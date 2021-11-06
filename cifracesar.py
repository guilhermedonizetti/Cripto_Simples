caracter = [
            'A','~','B',"|",'C','{','D','°','E','Ô','F','^','G',
            '=','H','"','I','9','J','8','K',"'",'L','N','f','_',
            'g','&','h','í','O','Q','W','#','X',';','Y','P','Z',
            '6','@','7',' ','a','ú','b',',','c','}','ª','d','e',
            '+','i','ç','j','.','k','0','l','ô','m','õ','n','ó',
            'o','ê','p','é','q','ã','r','à','s','â','t','á','u',
            'Ú','v','Õ','w','Ó','x','M','y','Í','z','1','Ê','2',
            'Ç','3','É','4','Á','5','R','À','S','Â','T','Ã','U',
            ')','V','\n','?','!',':','$','-','/','*','%','('
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
            #x recebe o indice da lista de caracteres onde esta o elemento atual + o tamanho da chave
            x = caracter.index(texto[i])-len(chave)
            if x>=0:
                nvtexto = nvtexto + caracter[x]
            else:
                nvtexto = nvtexto + caracter[len(caracter)+x]
        
        return nvtexto