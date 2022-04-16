#1017 - TORNEIO DE PÁSCOA - PROGRAMAÇÃO E ALGORITMOS ADS I

#Fórmula da Velocidade Média: Vm = Distancia / Tempo

tempo = int( input() )
vm = int( input() )

distancia = vm * tempo

#O automóvel faz 12 km/L ...
litros = distancia/12
print("%.3f" % litros)
