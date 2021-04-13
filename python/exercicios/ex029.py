vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('VOCE FOI MULTADO POR R${}!'.format((vel - 80) * 7))
else:
    print('Parabens, voce seguiu as regras do transito corretamente :)')
