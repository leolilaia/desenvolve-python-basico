#Solicita a idade de Cris e Juliana
Cris = int(input("Digite a idade de Cris: "))
Juliana = int(input("Digite a idade de Juliana: "))

#Verifica a idade de ambos
Permitido = Juliana > 17 and Cris > 17

#imprime o resultado na tela
print(Permitido)