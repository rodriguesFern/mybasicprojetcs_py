vel = int(input("Qual a velocidade do carro?"))

if vel > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h.")
    multa = (vel-80)*7
    print("Você pagará uma multa de R${}".format(multa))
elif vel < 0:
    print("Velocidade Invalida!")
else:
    print("Velocidade permitida na rodovia!")

print("Tenha um bom dia e dirija com segurança.")


