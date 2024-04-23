from sacar import sacar
from depositar import depositar
from extrato import extrato

saldo = 0
limite = 500
extrato_conta = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  print("""
  =====================================
  Digite a operação desejada:

  [1] Sacar
  [2] Deposito
  [3] Extrato 
  [0] Sair
  =====================================
  """)

  acao = int(input())

  if acao == 1:
    print("Qual valor deseja sacar?\n")
    valor = float(input())
    saldo, extrato_conta = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato_conta)

  elif acao == 2:
    print("Qual valor deseja depositar?\n")
    valor = float(input())
    saldo, extrato_conta = depositar(valor, saldo, extrato_conta)
    
  elif acao == 3:
    saldo, extrato_conta = extrato(saldo, extrato_conta)

  elif acao == 0:
    print("Obrigado por usar nosso sistema. Até mais!")
    break  # Sai do loop se a ação for zero

  else:
    print("Operação inválida!\n")

  print("\nExtrato atualizado:")
  extrato(saldo, extrato_conta)