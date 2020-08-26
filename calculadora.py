x = int(input("""Escolha um numero referente a conta que deseja fazer:
    1 - ADICAO
    2 - MULTIPLICACAO
    3 - SUBTRACAO
    4 - DIVISAO
    """))

if x == 1:
    n = int(input("Escolha o numero para tabuada:"))
    for i in range (1, 11):
        print(i ,"-", n ,"=", x+i)
elif x == 2:
    n = int(input("Escolha o numero para tabuada:"))
    for i in range (1, 11):
        print(i ,"-", n ,"=", x-i)
elif x == 3:
    n = int(input("Escolha o numero para tabuada:"))
    for i in range (1, 11):
        print(i ,"*", n ,"=", x*i)
elif x == 4:
    n = int(input("Escolha o numero para tabuada:"))
    for i in range (1, 11):
        print(i ,"/", n ,"=", "{:.2f}".format(x/i))
else:
    print ("Comando invalido!")

