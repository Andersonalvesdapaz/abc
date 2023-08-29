carro = int(input('qual a velocidade seu carro estar andando?'))
dinheiro = 7
multa = (carro-80)*dinheiro
if carro > 80:
    print('multado! vc exerdeu o limite permitido que é de 80km/h')
    print('vc deve pagar o uma multa no valor de {:.1f}'.format(multa))
print('tenha um bom dia diriga com segurança!')

