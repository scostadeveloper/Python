'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele'''


txt = input("Digite algo: ")
print('O que você digitou é do tipo: ',type(txt))
print("É um numero? ",txt.isalnum())
print('É alphanumerico?' ,txt.isalpha())