"""
nome = input("Qual é o seu nome?")
idade = input("Qaul é a sua idade?")
peso = input("Qual é o seu peso?")
print(nome, idade, peso)
"""


"""
                        #DESAFIO 01
    Crie um script Python que leia o nome de uma pessoa e mostre
    uma mensagem de boas-vindas de acordo com o valor digitado.
"""

nome = input("Digite o seu nome: ")
print("Seja bem vindo(a),",nome+"!")


"""
                        #DESAFIO 02
    Crie um script Python que leia o dia, o mês e o ano de nascimnento de uma
    pessoa e mostre uma mensagem com a data formatada.
"""

print("Digite a sua data de nascimento:")
dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")
print("Sua data de nascimento é: " +dia+ "/" +mes+ "/" +ano)


"""
    Crie um script Python que leia dois numeros e tente mostra a
    soma entre eles.
"""

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
soma = numero1 + numero2
print("O total da soma é: ",soma)
