sal = float(input('digite o valor do salario do funcionario'))
sup = sal / 100 * 10
inf = sal / 100 * 15
if sal > 1250:
    print('o aumento do funcionario vai ser de R${}, recebendo um total de R${}'
          .format(sup, sup + sal))
else:
    print('o aumento do funcionario vai ser de R${}, recebendo um total de R${}'
          .format(inf, inf + sal))
