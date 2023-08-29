frase = str(input(' digite uma frase')).upper().strip()
a = frase.count('A')
print('a letra A aparace {} vezes na frase'.format(a))
print(' em qual posição o A apareece pela a primeira vez na posição {}'.format(frase.find('A')+1))
print(' em qual posição o A apareceu pela ultima vez na posição {}'.format(frase.rfind('A')+1))



