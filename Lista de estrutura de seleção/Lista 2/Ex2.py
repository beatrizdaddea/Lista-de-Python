"""2.Escreva um programa que leia três números e que imprima o maiore o menor."""

num_1 = float(input('Primeiro numero: '))
num_2 = float(input('Segundo numero : '))
num_3 = float(input('Terceiro numero: '))

if (num_1 < num_2) and (num_1 < num_3):
    print("Menor: ", num_1)
    if num_2 > num_3:
        print("Maior: ", num_2)
    else:
        print("Maior: ", num_3)
elif (num_2 < num_1) and (num_2 < num_3):
    print("Menor: ", num_2)
    if num_1 > num_3:
        print("Maior: ", num_1)
    else:
        print("Maior: ", num_3)
else:
    print("Menor: ", num_3)
    if num_1 > num_2:
        print("Maior: ", num_1)
    else:
        print("Maior: ", num_2)
