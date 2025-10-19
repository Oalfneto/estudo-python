l=int(input('Digite a largura da parede:'))
h=int(input('Digite a altura da parede:'))
a=l*h
t=a/2
print('Você precisará de {} litros de tinta para pintar a parede'.format(t))
P=t*30
print('Você iria gastar {} reais para comprar a tinta'.format(P))
print('mas ...\nFoi Sortudo e Ganhou um desconto de 5%\nAgora terá que pagar {}'.format(P*(95/100)))