""""7.Faça um programa que dados três valores X, Y e Z, verificase eles podem ser os comprimentos dos lados de um triânguloe, se forem, verificar se é um triângulo equilátero, isósceles ou escaleno. Caso eles não formem um triângulo, escreva uma mensagem."""

x = float(input('Digite x: '))
y = float(input('Digite y: '))
z = float(input('Digite z: '))

if (x + y < z) or (x + z < y) or (y + z < x):
    print('Não é um triangulo.')

elif (x == y) and (x == z):
    print('É um triangulo: Equilátero.')

elif (x == y) or (x == z) or (y == z):
    print('É um triangulo: Isósceles')

else:
    print('É um triangulo: Escaleno')
