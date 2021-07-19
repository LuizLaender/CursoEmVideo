print('me fale a largura e a altura de sua parede para podermos pintar ela')
al = float(input('altura da parede'))
la = float(input('largura da parede'))
area = al*la
tinta = area/2
print('Sua parede tem dimensão de {}m²x{}m² e sua area é de {}m²'.format(al, la, area))
print('Para pintar esta parede, voce precisará de {}l de tinta'.format(tinta))
