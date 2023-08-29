import math
ag = float(input('digite o angulo que vc deseja:'))
cos =  math.cos(math.radians(ag))
seno = math.sin(math.radians(ag))
tan = math.tan(math.radians(ag))
print('o angulo de {} tem o seno de {:.2f}'.format(ag, seno))
print('o angulo de {} tem o cosseno de {:.2f}'.format(ag, cos))
print('o angulo de {} tem a tangente de {:.2f}'.format(ag, tan))


