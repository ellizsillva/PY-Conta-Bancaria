from sacar import sacar
from depositar import depositar

saldo = 0
print("Bom dia! Gostaria de realizar um saque ou um deposito?")
acao = input()

if acao == "deposito":
  print("Qual valor a ser depositado?")
  valor = int(input())
  depositar(valor, saldo)
  #saldo = depositar(valor, saldo)

else:
  print("Qual valor deseja sacar?")
  valor = int(input())
  sacar(valor, saldo)
  #saldo = sacar(valor, saldo)

