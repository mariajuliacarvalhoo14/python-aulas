texto = input ("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print (letra, end="")

 
print() #serve para adicionar uma uma de linha
