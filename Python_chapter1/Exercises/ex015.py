km = float(input('digite a kilometragem'))
dias = float(input('por quantos dias ele foi alugado?'))
total = (km * 0.15) + (dias * 60)
print('o valor total do aluguel do carro foi R${:.2f}'.format(total))
