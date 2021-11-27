#Programa para gerar hash de 3 digitos para qualquer entrada de texto

class Hash:

	def __init__(self):
		self.caracteres = [
			'A','B','C','D','E','F','G','H','I','J','K','L','M',
			'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '
		]

	#Metodo que recebe entrada de texto
	def EntradaTexto(self):
		texto = input("Digite: ")
		if len(texto)>100:
			print("Digite no máximo 100 caracteres.\n")
			self.EntradaTexto()
		else:
			texto = texto.upper()
			print("\n{}\n".format(texto))
			valor = self.CalcularTamanho(texto)
			self.CalcularHash(valor, len(texto))

	#Metodo que gera um valor para cada caracter para posteriormente calcular o hash
	def CalcularTamanho(self, texto):
		resul = 0
		for i in texto:
			valor = self.caracteres.index(i) * len(texto)
			resul = resul + valor
		return resul

	#Metodo que gera um hash de acordo com o valor dos caracteres
	def CalcularHash(self, valor, tam):
		i_hash = valor % 100
		i_hash = "000"+str(i_hash)
		print("\nHash: {}".format(i_hash[-3::]))

g_hash = Hash()
g_hash.EntradaTexto()