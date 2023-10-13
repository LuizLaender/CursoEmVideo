preco = float(input('Valor do produto sem desconto: R$'))
vista = preco - (10/100*500)
parcela = preco + (8/100*500)
print('O valor do produto é de R${:.2f}, mas se pagar a vista ele sai por R${:.2f}, e se pagar parcelado, sai por {:.2f}'.format(preco, vista, parcela))
