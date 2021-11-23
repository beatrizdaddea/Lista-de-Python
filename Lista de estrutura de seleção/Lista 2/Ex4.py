"""4.Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você  deve  poder  calcular  a  soma  (+),  subtração  (-),multiplicação  (*)  e  divisão  (/).  Exiba  o resultado da operação solicitada."""

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))

operação = input("Digite a operação a realizar (+,-,* ou /):")

if operação == "+":
    resultado = a + b

elif operação == "-":
    resultado = a - b

elif operação == "*":
    resultado = a * b

elif operação == "/":
    resultado = a / b

else:
    print("Operação inválida!")
    resultado = 0


print("Resultado: ", resultado)
