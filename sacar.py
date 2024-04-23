def sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato_conta):

    #verifica se o valor do saque é maior do que o saldo disponível na conta
    excedeu_saldo = valor > saldo

    #verifica se o valor do saque é maior do que o limite permitido
    excedeu_limite = valor > limite

    #verifica se o número de saques já realizados atingiu ou excedeu o limite permitido
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    #imprime a informação de saldo insuficiente
    if excedeu_saldo:
        print("Operação não permitida. Você não tem saldo suficiente.")
    
    #imprime a informação de limite excedido
    elif excedeu_limite:
        print("Operação não permitida. O valor do saque excedeu o limite.")

    #imprime a informação de limite indisponivel
    elif excedeu_saque:
        print("Operação não permitida. Número máximo de saques excedido")

    #executa a ação de saque, atualiza saldo e imprime o extrato
    elif valor > 0:
        saldo -= valor
        print("Saque realizado com sucesso!")
        extrato_conta += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    #informado saldo insuficiente se o saldo for maior que o saque    
    else:
        print("Saldo insuficiente")
        print("Seu saldo atual é de:", saldo)

    return saldo, extrato_conta