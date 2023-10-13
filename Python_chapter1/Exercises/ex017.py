from math import hypot
cat = float(input('digite o cateto oposto do triangulo: '))
adj = float(input('digite o cateto adjacente do triangulo: '))
hyp = hypot(cat, adj)
print('o valor da hipotenusa é {:.2f}'.format(hyp))
