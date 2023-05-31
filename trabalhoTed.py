# variáveis (guardar informações)
# operadores aritméticos (somar/dividir)
# inputs (entrada e leitura de dados)
print('---Programa de Cálculo de Média---')
input(statiscas)
nota1: float = float(input("Digite o primeiro valor:"))
nota2 = float(input("Digite o segundo valor:"))
nota3 = float(input("Digite o segundo valor:"))
media = (nota1 + nota2 + nota3) / 3
print(f'A média entre {nota1} e {nota2} e  {nota3} é igual a {media}')

print('---Conversão de C para F ---')
tempCel = float(input('Digite a temperatura em Celsius:'))
print(f'A temperatura {tempCel} em C corresponde a {(9 * tempCel + 160) / 5} em Fahrenheit')

print('---AFERIÇÃO DE PARIDADE---')
valor = int(input("Digite um valor inteiro:"))
if valor % 2 == 0:
    print(f"O valor {valor} é PAR")
else:
    print(f"O valor {valor} é ÍMPAR")
