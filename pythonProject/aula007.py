n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
'''O comando {:,2f} especifica quantas casas decimais o valor vai ter, o comando end='' especifica
 o que vai ter ao final da linha, no caso ele exibe apenas um espaço, logo o print a baixo ficará na mesma linha'''
'''O comando \n serve para quebrar a linha'''
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))