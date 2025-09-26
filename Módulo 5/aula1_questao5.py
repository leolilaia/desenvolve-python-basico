#Biblioteca
import emoji

# Mostrar a lista para o usuário
print("Emojis disponíveis:\n")
print("😎  - :sunglasses:")
print("🥶  - :cold_face:")
print("🦊  - :fox:")
print("👍  - :thumbs_up:")
print("💙  - :blue_heart:")
print("🤍  - :white_heart:\n")

# Entrada do usuário
frase = input("Digite uma frase usando os códigos acima:\n")

# Transformar a frase em emojis
frase_emojizada = emoji.emojize(frase, language="alias")

# Saída
print("\nFrase emojizada:\n")
print(frase_emojizada)
