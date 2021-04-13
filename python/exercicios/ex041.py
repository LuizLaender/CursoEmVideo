from datetime import date
anonasci = int(input('digite o ano de nascimento do nadador'))
ano = date.today().year
idade = ano - anonasci
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUVENIL')
elif idade == 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')
