
opcao= int(input("\nInforme uma opção:\n[1]sacar \n[2] exibir extrato\n"))

if opcao==1:
    valor= float(input("\nInforme a quantia que deseja sacar\n"))

elif opcao==2:
    print("\nExibindo o extrato:\n")

else:
    print("Opção inválida")
    #4sys.exit("\nOpção imválida\n")