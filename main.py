import functions as fc

class Cripto_Simples:

    #Cria um menu de 3 opcoes para o usuario
    def Menu(self):
        op = int(input("1) Criptografar - Cesar\n2) Decriptografar - Cesar\n3) Sair\n"))
        if op==1:
            self.criptografar_com_cesar()
        if op==2:
            self.decriptografar_com_cesar()
        if op==3:
            exit()
        if op<1 or op>3:
            print("Opção inválida!\n")
            self.Menu()
    
    #criptografar usando a Cifra de Cesar
    def criptografar_com_cesar(self):
        texto = input("Digite seu texto: ") #recebe o texto puro
        chave = input("Digite a chave: ") #recebe o valor da chave
        resul = fc.criptografar_cesar(texto, chave)
        if resul == False:
            print("A chave deve ser menor que o texto.\n")
            self.criptografar_com_cesar()
        else:
            print("\nResultado: {}\n".format(resul))
    
    #decriptografar usando a Cifra de Cesar
    def decriptografar_com_cesar(self):
        texto = input("Digite seu texto: ") #recebe o texto puro
        chave = input("Digite a chave: ") #recebe o valor da chave
        resul = fc.decriptografar_cesar(texto, chave)
        if resul == False:
            print("A chave deve ser menor que o texto.\n")
            self.criptografar_com_cesar()
        else:
            print("\nResultado: {}\n".format(resul))

c_simples = Cripto_Simples()
c_simples.Menu()