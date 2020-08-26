from datetime import date
ano = int(input("Digite o seu ano de nascimento:"))
atual = date.today().year
idade = atual-ano
if ano <= 1899 or ano >= 3000:
    print("ANO INVALIDO - PROGRAMA APENAS DE 1900 A 2999")
else:
    print("Quem nasceu no ano de {} tem {} anos em {}.".format(ano, idade,atual))
    if idade == 18:
     print("Esse é o ano do seu alistamento!")
    elif idade > 18:
     print("Ja passou da hora de voce se alistar, espero que ja tenha feito!")
     print("Seu ano correto de alistamento era em {}!".format(ano+18))
    elif idade < 18:
     print("Ainda faltam {} anos para o seu alistamento.".format(18-idade))
    else:
      print("COMANDO INVALIDO!")