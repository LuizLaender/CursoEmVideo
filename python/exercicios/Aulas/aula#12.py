nome = str(input('qual eh o seu nome?'))

if nome == 'Gustavo':
    print('que nome bonito')
elif nome == 'Luiz' or nome == 'pedro' or nome == 'julia':
    print('que nome bonito')
elif nome in 'Clairo Mônica Raquel':
    print('seu nome eh bem comum')
else:
    print('que nome feio')

print('tenha um bom dia {}'.format(nome))
