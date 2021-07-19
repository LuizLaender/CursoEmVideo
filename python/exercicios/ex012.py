valor = float(input('qual o preço do produto? R$'))
novo = valor - (5/100*valor)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% ele vai custar R${:.2f}'.format(valor, novo))
