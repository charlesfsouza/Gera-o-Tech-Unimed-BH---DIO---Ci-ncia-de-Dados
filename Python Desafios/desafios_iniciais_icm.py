entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if (distancia > 0 and distancia < 1000) and (diametro1 > 0 and diametro1 < 100) and (diametro2 > 0 and diametro2 < 100):

    ICM = distancia / (diametro1 + diametro2)
    print(f"{ICM:.2f}")

else:
    print("Informe parâmetros válidos")
  