dias = float(input('quantos dias alugados?'))
km = float(input('quantos km eu rodados?'))
diaria = dias*60
diriakm = km * 0.15
alguel = diaria + diriakm
print('o total a pagar foi de {}'.format(alguel))