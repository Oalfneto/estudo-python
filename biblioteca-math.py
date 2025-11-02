from math import cos,sin,tan,radians
a=float(input("Digite o ângulo que você deseja:"))
a=radians(a)
seno=sin(a)
cosseno=cos(a)
tangente=tan(a)
print("Valores:\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}".format(seno,cosseno,tangente))
