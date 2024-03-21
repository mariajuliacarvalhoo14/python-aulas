MAIOR_IDADE = 18 #variável
IDADE_ESPECIAL= 17
idade = int(input("\nInforme sua idade\n"))

if idade >= MAIOR_IDADE:
   print("Pode tirar CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode ASSISTIR aulas TÉORICAS")
else:
    print("Ainda não pode tirar CNH.")