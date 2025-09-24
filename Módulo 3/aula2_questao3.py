#Entrada de dados
idade = int(input("Digite a sua idade: "))
jogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitorias = int(input("Quantos jogos já venceu? "))

#Verifica se o jogador está dentro das condições
resultado = (16 <= idade <= 18) and jogos and (vitorias >= 1)

#Imprime o resultado
print("Apto para ingressar no clube de jogos de tabuleiro: ", resultado)