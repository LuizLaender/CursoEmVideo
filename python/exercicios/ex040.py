nota1 = int(input('digite a nota da sua primeira prova'))
nota2 = int(input('digite a nota da sua segunda prova'))

media = (nota1 + nota2) / 2

if media < 5:
    print('reprovado')
elif 5 <= media <= 6.7:
    print('recuperacao')
else:
    print('aprovado')
