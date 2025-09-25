#Entrada de dados
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#calcula a media das notas
m = (n1 + n2 + n3)/3

#verifica a condição
if m>=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")

#Saída
print("Fim")