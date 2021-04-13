valor = float(input('Qual é o salário do funcionário? R$'))
salario = valor + (15 / 100 * valor)
print('Um funcionário que ganhava R${:.2f}, agora com 15% de aumento, passou a receber R${:.2f}'.format(valor, salario))
