a = 'Luiz Laender'


cores = {'limpa': '\033[m',
         'azul': '\033[36m',
         'verde': '\033[32m',
         'amarelo': '\033[33m'}

print('Olá {}{}{} que bom te ver!!'.format(cores['verde'], a, cores['limpa']))
