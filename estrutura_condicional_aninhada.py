conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 500
cheque_especial = 450
conta_especial= 30000
if conta_normal:
    if saldo >= saque:
        print ("saque realizado com sucesso")
    elif saque <= (saldo+cheque_especial):
        print("Saque realizado com sucesso com uso de cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print ("Saldo insuficiente")

