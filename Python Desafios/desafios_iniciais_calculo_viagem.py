base_dados = input().split()

tempo = int(base_dados[0]) # Numero total de cachorros-quentes
velocidade = int(base_dados[1]) # Numero total de participantes na competicao
km_por_litro = 12

if (tempo >= 0) and (velocidade >= 0):

    litros_total = (tempo * velocidade) / km_por_litro
    print(f"{litros_total:.3f}")

else:
    print("Informe parâmetros válidos")
  