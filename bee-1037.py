#1037 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

numero = float( input() )

# < 0 ?
if numero < 0:
    print("Fora de intervalo")
elif numero >= 0 and numero <= 25: # [0,25] ?
    print("Intervalo [0,25]")
elif numero > 25 and numero <= 50: # (25,50] ?
    print("Intervalo (25,50]")
elif numero > 50 and numero <= 75: # (50,75] ?
    print("Intervalo (50,75]")
elif numero > 75 and numero <= 100: # (75,100] ?
    print("Intervalo (75,100]")
else: # > 100 !
    print("Fora de intervalo")
