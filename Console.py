import random

print("=" * 40)
print("Fortune Tiger")
print("=" * 40)

ValorSaldo = float(input("Digite o valor do saldo: "))
jogadas = 0

while True:
    print("1 - fortune tiger")
    print("2 - foguete da sorte")
    print("3 - jokenpo")
    print("4 - sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        if ValorSaldo >= 10:
            print("bem vindo ao fortune tiger")
            print("1 - jogar")
            print("2 - sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                print("Jogando...")
                ValorSaldo -= 10
                jogadas += 1
                if jogadas <= 3:
                    ganho = random.choice([10, 20])
                    ValorSaldo += ganho
                    print(f"Você ganhou R$ {ganho}!")
                else:
                    resultado = random.choice(["ganhou", "perdeu", "neutro"])
                    if resultado == "ganhou":
                        ganho = random.choice([10, 20])
                        ValorSaldo += ganho
                        print(f"Você ganhou R$ {ganho}!")
                    elif resultado == "perdeu":
                        print("Você perdeu a aposta.")
                    else:
                        ValorSaldo += 10
                        print("Você manteve o valor da aposta.")
                print("Saldo atual: R$ ", ValorSaldo)
            else:
                print("Saindo...")
        else:
            print("Saldo insuficiente")
    elif opcao == 2:
        if ValorSaldo >= 5:
            print("bem vindo ao foguete da sorte")
            print("1 - jogar")
            print("2 - sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                print("Jogando...")
                ValorSaldo = ValorSaldo - 5
                print("Saldo atual: R$ ", ValorSaldo)
            else:
                print("Saindo...")
        else:
            print("Saldo insuficiente")
    elif opcao == 3:
        if ValorSaldo >= 2:
            print("bem vindo ao jokenpo")
            print("1 - jogar")
            print("2 - sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                print("Jogando...")
                ValorSaldo = ValorSaldo - 2
                print("Saldo atual: R$ ", ValorSaldo)
            else:
                print("Saindo...")
        else:
            print("Saldo insuficiente")
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida")
print("Fim do programa")
print("=" * 40)
