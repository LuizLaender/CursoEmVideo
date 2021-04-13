tempo = int(input('quantos anos o seu carro tem? '))
#if tempo <= 3:
#    print('carro novo')
#else:
#    print('carro velho')
print('carro novo' if tempo <= 3 else 'carro velho')
print('----FIM----')
#----------------------------------------------------
nome = str(input('qual é o seu nome?'))
if nome == 'Gustavo':
    print('que nome feio vc tem')
else:
    print('seu nome é tão comum...')
print('bom dia, {}'.format(nome))
#----------------------------------------------------
n1 = float(input('digite a primeira nota'))
n2 = float(input('digite a segunda nota'))
m = (n1 + n2) / 2
print('a sua media foi {:.1f}'.format(m))
print('parabens!' if m >= 6 else 'estude mais!')
