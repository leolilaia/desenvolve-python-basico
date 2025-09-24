#Solicita a idade de Cris e Juliana
Cris = int(input("Digite a idade de Cris: "))
Juliana = int(input("Digite a idade de Juliana: "))

#Verifica a idade de ambos(desta vez utilizando o "or" no lugar do "and")
Permitido = Juliana > 17 or Cris > 17

#imprime o resultado na tela
print(Permitido)