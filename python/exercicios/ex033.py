print('Digite 3 numeros inteiros')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
#------------------------------------------------------------------
if n1 == n1 > n2 > n3:
    print('o maior eh o primeiro num, e o menor eh o terceiro')
if n2 == n2 > n3 > n1:
    print('o maior eh o segundo num, e o menor eh o primeiro')
if n3 == n3 > n1 > n2:
    print('o maior eh o terceiro num, e o menor eh o segundo')
if n1 == n1 < n2 < n3:
    print('o maior eh o terceiro numero, e o menor eh o primeiro')
if n2 == n2 < n3 < n1:
    print('o maior eh o primeiro numero, e o menor eh o segundo')
if n3 == n3 < n1 < n2:
    print('o maior eh o segundo numero, e o menor eh o terceiro')
#------------------------------------------------------------------
