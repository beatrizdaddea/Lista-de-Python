"""5.Escreva  um  programa  que  calcule  o  preço  a  pagar  pelo  fornecimentode  energia  elétrica. Pergunte  a  quantidade  de  kWh  consumida  e  o  tipo  de  instalação:R  para  residências,  I  para indústrias e C para comércios. Calcule o preço apagar de acordo com a tabela a seguir."""

consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")

if tipo == "R":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65

elif tipo == "I":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60

elif tipo == "C":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60

else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço


print(f"Valor a pagar: R$ ", custo)
