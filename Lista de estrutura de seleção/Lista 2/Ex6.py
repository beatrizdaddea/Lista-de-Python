"""6.Um ano bissexto pode ser calculado verificando se ele é divisível por 4. Caso não seja divisívelpor 4, ele não é bissexto. Caso seja divisívelpor 4, deve-se verificar se ele é divisível por 100. Caso não seja divisível por 100, ele é bissexto. Caso seja divisível por 100, deve-se verificar se ele  é  divisível  por  400.  Caso  seja divisível  por  400,  ele  é  bissexto.  Caso  não  seja  divisível  por 400, ele não é bissexto. Escreva um programa que peça ao usuário que ele digite um ano e calcule se o ano digitado é bissexto ou não."""

Ano = int(input('Digite o ano: '))

if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print(' O ano é bissexto')

else:
    print('O ano não é bissexto')
