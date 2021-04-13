d = float(input('Digite a distancia da sua viagem: '))
valor = d * 0.50 if d <= 200 else d * 0.45
print('o valor da sua passagem é de R${:.2f}'.format(valor))
