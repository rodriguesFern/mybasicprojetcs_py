from random import randint
from time import  sleep #delay para passar de linha

print("-=-" * 20)
print("Vou pensar em um numero de 0 a 5, tente adivinhar...")
print("-=-" * 20)

numeror = randint (0,5)
numero = int(input("Que numero eu pensei:"))

if numero == numeror:
    print("Processando ...")
    sleep(2)
    print("ACERTOU! Eu pensei no número {}".format(numeror))
elif numero >= 6 or numero <= -1:
    print("Numero Inválido! Não atrapalha a brincadeira! :(")
elif numero != numeror:
    print("Processando ...")
    sleep(2)
    print("ERROU! Eu pensei no numero {}, e não em {}.".format(numeror, numero))
