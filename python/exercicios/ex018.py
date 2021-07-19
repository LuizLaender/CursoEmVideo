from math import radians, cos, tan, sin
num = float(input('digite o valor do ângulo: '))
sin = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print('O ângulo de {:.0f}° é equivalente a: '.format(num))
print('SENO: {:.2F}°'.format(sin))
print('COSSENO: {:.2f}°'.format(sin))
print('TANGENTE: {:.2f}°'.format(tan))
