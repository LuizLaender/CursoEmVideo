print('digite dois numeros')
n1 = int(input('primeiro numero'))
n2 = int(input('segundo numero'))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
p = n1 ** n2
print('a soma eh {}, a divisao eh {},\na multiplicacao eh {}'.format(s, d, m), end='')
print(' a divisao inteira eh {} e a potencia eh {}'.format(di, p), end=' >>> ')
