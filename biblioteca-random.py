from random import choice
a1=input("Digite o nome do primeiro aluno:")
a2=input("Digite o nome do segundo aluno:")
a3=input("Digite o nome do terceiro aluno:")
lista=[a1,a2,a3]
escolhido=choice(lista)
print("O aluno escolhido foi {}".format(escolhido))
