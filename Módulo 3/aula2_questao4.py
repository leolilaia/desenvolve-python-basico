#Entrada de dados
classe = (input("Escolha a classe (guerreiro, mago ou arqueiro): "))
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

#Verificação das condições
resultado = (
    (classe == "guerreiro" and forca >= 15 and magia <= 10) 
    or (classe == "mago" and forca <= 10 and magia >= 15) 
    or (classe == "arqueiro" and 5 < forca <= 15 and 5 < magia <= 15)
)

#Imprime o resultado na tela
print("Pontos de atributo consistentes com a classe escolhida: ", resultado)