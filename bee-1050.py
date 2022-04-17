#1050 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

ddd = int( input() )

#Lá vem muitos ifs...
if ddd == 61:
    print("Brasilia")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("Sao Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitoria")
elif ddd == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")

#Esse algoritmo fica melhor com a estrutura Dicionários ...