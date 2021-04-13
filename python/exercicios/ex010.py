real = float(input('quantos reais voce tem na sua carteira? R$'))
dolares = real / 5.38
euro = real / 6.52
rupia = real / 0.074
print('com {:.2f} reais voce pode comprar {:.2f} dolares, {:.2f} euros e {:.2f} rupias'.format(real, dolares, euro, rupia))
