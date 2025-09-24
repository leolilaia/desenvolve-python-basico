#Entrada de Dados
genero = (input("Digite o seu gênero(M para Masculino, F para Feminino): "))
idade = int(input("Digite a sua idade: "))
tempo = int(input("Digite o seu tempo de serviço(em anos): "))

#Verifica se a pessoa já pode aposentar
aposentar = (
    (genero == "M" and (idade >= 65 or tempo > 30 or (idade >= 60 and tempo >= 25)))
    or (genero == "F" and (idade >= 60 or tempo > 30 or (idade >= 60 and tempo >= 25)))
)

#Imprime o resultado na tela
print("Já pode se aposentar: ", aposentar)