print('digite o comprimento de 3 retas para ver se eh possivel formar um triangulo com elas')
r1 = float(input('reta 1'))
r2 = float(input('reta 2'))
r3 = float(input('reta 3'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode formar um triangulo')
else:
    print('nao pode formar um triangulo')

'''if r1 > r2 > r3:
    hip = r1
    res = r2 + r3
if r1 > r3 > r2:
    hip = r1
    res = r3 + r2
if r2 > r3 > r1:
    hip = r2
    res = r3 + r1
if r2 > r1 > r3:
    hip = r2
    res = r1 + r3
if r3 > r1 > r2:
    hip = r3
    res = r1 + r2
if r3 > r2 > r1:
    hip = r3
    res = r2 + r1

if hip < res:
    print('eh possivel')
else:
    print('nao eh possivel')'''
