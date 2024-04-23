def depositar(valor, saldo, extrato_conta):
    if valor > 0:
        saldo += valor
        extrato_conta += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("Valor para depósito não válido. Tente novamente.")

    # Retornar o novo saldo e o extrato atualizado
    return saldo, extrato_conta