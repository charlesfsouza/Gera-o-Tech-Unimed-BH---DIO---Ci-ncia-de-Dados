base_dados = input().split()

H = int(base_dados[0]) # Numero total de cachorros-quentes
P = int(base_dados[1]) # Numero total de participantes na competicao


if (H >= 1 and H <= 1000) and (P >= 1 and P <= 1000):

    media = H / P
    print(f"{media:.2f}")

else:
    print("Informe parâmetros válidos")
  