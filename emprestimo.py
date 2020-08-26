casa = float(input("Qual o valor da casa em R$?"))
sal = float(input("Qual o seu salario em R$?"))
ano = int(input("Com quantos anos você deseja pagar?"))

parc = (casa/ano)/12
cond =sal*30/100

'''print(parc)
print(cond)'''

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(casa, ano, parc))

if parc > cond:
    print("Emprestimo NEGADO!")
else:
    print("Emprestimo APROVADO!")



