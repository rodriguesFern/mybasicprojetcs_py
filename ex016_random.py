from random import choice

a = str(input("Digite o nome do primeiro aluno:"))
b = str(input("Digite o nome do segundo aluno:"))
c = str(input("Digite o nome do terceiro aluno:"))
d = str(input("Digite o nome do quarto aluno:"))

lista = [a, b, c, d]
choice(lista)
print ("O aluno sorteado foi {}".format(lista))