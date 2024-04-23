def extrato(saldo, extrato_conta):
    print("\n================= EXTRATO ==================")
    print("Não foram realizadas movimentações" if not extrato_conta else extrato_conta)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================================")
    
    return saldo, extrato_conta
