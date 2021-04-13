print('digite o valor de 3 retas para formarem um triangulo')
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('forma um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('nao forma um triangulo')
