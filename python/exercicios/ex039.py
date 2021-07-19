from datetime import date
anonasci = int(input('digite o seu ano de nascimento'))
ano = date.today().year
idade = ano - anonasci
if idade < 18:
    print('ainda nao se alistou')
elif idade > 18:
    print('ja se alistou')
else:
    print('esta na hora de se alistar')
