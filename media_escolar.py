x = float(input("Digite a primeira nota:"))
y = float(input("Digite a segunda nota:"))

media = (x+y)/2
if x > 10 or y > 10:
    print("NOTA INVALIDA - PROGRAMA DE NOTAS ATÉ 10.")
elif x < 0 or y < 0:
    print("NOTA INVALIDA - PROGRAMA NAO RECONHECE NOTAS NEGATIVAS.")
else:
    print("Tirando {} e {}, a média é do aluno é {}".format(x, y, media))
    if media >= 7.0:
        print("O aluno foi APROVADO!")
    elif media >= 5.0 and  media < 7.0:
        print("O aluno está de RECUPERAÇÃO!")
    elif media < 5.0:
        print("O aluno foi REPROVADO")
