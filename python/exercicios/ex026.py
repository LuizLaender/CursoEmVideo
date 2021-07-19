frase = str(input('digite uma frase')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira vez que a letra A aparece é na casa {}'.format(frase.find('A')+1))
print('a posicao que a letra a aparece pela ultima vez é na casa {}'.format(frase.rfind('A')+1))
