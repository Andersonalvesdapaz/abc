num = int(input('digite um numero'))
u = num // 1 %10
d = num // 10 % 10
ce = num // 100 % 10
m = num // 1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('a centena {}'.format(ce))
print('a milhar é {}'.format(m))


