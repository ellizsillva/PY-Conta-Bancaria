def sacar(valor, saldo):
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso")
        print("Seu saldo atual é de:", saldo)
    else:
        print("Saldo insuficiente")
        print("Seu saldo atual é de:", saldo)
    return saldo
