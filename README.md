<h1 align="center">Cripto_Simples</h1>
<p align="center">
  :lock: Um simples prorama em Python que executa a Cifra de César e Permutação. :lock:
</p>

<b>Objetivo: </b>o objetivo do progra é aplicar técnicas simples de criptografia em linguagem de programação. o programa aplica a técnica da Cifra de César e de Permutação.

<b>Cifra de César: </b>é uma técnica de substituição de caracteres. Inicialmente, existe uma lista de caracteres e um texto a ser criptografado, então o algoritmo: percorre o texto passando por cada letra; procura essa letra na lista de caracteres; seleciona o caracter que está a X posições a frente; gera o novo texto. Exemplo:

```python
letra = "G"
chave = "python"

lista_de_caracteres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

#Em qual posicao da lista se encontra o valor de 'letra' ? No indice 6.
#Qual o tamanho da chave ? Tamanho igual a 5
#Entao, a partir do indice 6, avance mais 5 posicoes e e selecione o valor

posicao = lista_de_caracteres.index(letra)
tamanho = len(chave)
nova_letra = lista_de_caracteres[posicao + tamanho]

print(nova_letra)
#> M
```

Esse método de criptografia usa aritmética modular, pois quando o algoritmo não tiver mais caracteres a frente será necessário retroceder ao índice inicial da lista. No caso do programa desse repositório, a quantidade de posições a frente para que o algoritmo selecione será igual ao tamanho da chave informada.
