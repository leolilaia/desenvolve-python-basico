#Entrada de dados
ano = int(input("Insira um ano para verificarmos se ele é bissexto: "))

#Verifica se o ano é bissexto ou não e imprime na tela
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Bissexto")
else:
    print("Não Bissexto")