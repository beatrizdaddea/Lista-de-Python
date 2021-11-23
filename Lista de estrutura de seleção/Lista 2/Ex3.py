""""3.Escreva um programa que pergunte o salário do funcionário e calculeo valor do aumento. Para salários superiores
a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%."""

salario = float(input('Digite seu salário: '))
pc_aumento = 0.10
pc_aumento_2 = 0.15

if salario > 1250:
    aumento_superior = salario * pc_aumento
    salario_novo = aumento_superior + salario
    print(f' Seu aumento foi de R${aumento_superior}, portanto seu novo salário é R$ {salario_novo}')

elif salario <= 1250:
    aumento_inferior = salario * pc_aumento_2
    salario_novo = aumento_inferior + salario
    print(f' Seu aumento foi de R${aumento_inferior}, portanto seu novo salário é R$ {salario_novo}')
