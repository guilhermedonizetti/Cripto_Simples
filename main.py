import cifracesar as cc
import permutacao as pm

class Cripto_Simples:

    #Cria um menu de 3 opcoes para o usuario
    def menu(self):
        print("1) Criptografar - Cesar\n2) Decriptografar - Cesar")
        print("3) Criptografar - Permuta\n4) Decriptografar - Permuta\n5) Sair")
        op = int(input())
        if op == 1:
            self.criptografar_com_cesar()
        if op == 2:
            self.decriptografar_com_cesar()
        if op == 3:
            self.criptografar_com_permutacao()
        if op == 4:
            self.decriptografar_com_permutacao()
        if op==5:
            exit()
        if op<1 or op>5:
            print("Opção inválida!\n")
            self.menu()
    
    #criptografar usando a Cifra de Cesar
    def criptografar_com_cesar(self):
        texto = input("Digite seu texto: ") #recebe o texto puro
        chave = input("Digite a chave: ") #recebe o valor da chave
        resul = cc.criptografar_cesar(texto, chave)
        if resul == False:
            print("A chave deve ser menor que o texto.\n")
            self.criptografar_com_cesar()
        else:
            print("\nResultado: {}\n".format(resul))
        self.menu()
    
    #decriptografar usando a Cifra de Cesar
    def decriptografar_com_cesar(self):
        texto = input("Digite seu texto: ") #recebe o texto puro
        chave = input("Digite a chave: ") #recebe o valor da chave
        resul = cc.decriptografar_cesar(texto, chave)
        if resul == False:
            print("A chave deve ser menor que o texto.\n")
            self.criptografar_com_cesar()
        else:
            print("\nResultado: {}\n".format(resul))
        self.menu()
    
    #criptografar usando a permuacao
    def criptografar_com_permutacao(self):
        texto = input("Texto: ")
        resul = pm.criptografar_permuta(texto)
        print("\nResultado: {}\n".format(resul))
        self.menu()

    #decriptografar usando a permuacao
    def decriptografar_com_permutacao(self):
        texto = input("Texto: ")
        resul = pm.decriptografar_permuta(texto)
        print("\nResultado: {}\n".format(resul))
        self.menu()

c_simples = Cripto_Simples()
c_simples.menu()