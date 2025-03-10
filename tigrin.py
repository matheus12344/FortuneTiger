import random
import matplotlib.pyplot as plt
import csv
import os

print("=" * 40)
print("Fortune Tiger")
print("=" * 40)

ValorSaldo = float(input("Digite o valor do saldo: "))
jogadas = 0
resultados = []

def load_results():
    global resultados
    if os.path.exists('resultados.csv'):
        with open('resultados.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                resultados.append(float(row[1]))

def start_game():
    global ValorSaldo, jogadas, resultados
    load_results()

# Load existing results from CSV if it exists
if os.path.exists('resultados.csv'):
    with open('resultados.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            resultados.append(float(row[1]))

while True:
    print("1 - fortune tiger")
    print("2 - foguete da sorte")
    print("3 - jokenpo")
    print("4 - sair")
    print("5 - exportar resultados para CSV")
    print("6 - comparar resultados em gráfico")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        if ValorSaldo >= 10:
            while True:
                print("bem vindo ao fortune tiger")
                print("1 - jogar")
                print("2 - sair")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    print("Jogando...")
                    aporte = float(input("Digite o valor do aporte: "))
                    if aporte > ValorSaldo:
                        print("Aporte maior que o saldo")
                        break
                    elif aporte < 10:
                        print("Aporte menor que o mínimo permitido")
                        break
                    else:
                        ValorSaldo -= aporte
                        jogadas += 1
                        if jogadas <= 3:
                            ganho = random.choice([aporte*2, aporte*3])
                            ValorSaldo += ganho
                            print(f"Você ganhou R$ {ganho}!")
                        else:
                            resultado = random.choice(["ganhou", "perdeu", "neutro"])
                            if resultado == "ganhou":
                                ganho = random.choice([aporte, aporte*2])
                                ValorSaldo += ganho
                                print(f"Você ganhou R$ {ganho}!")
                            elif resultado == "perdeu":
                                print("Você perdeu a aposta.")
                            else:
                                ValorSaldo += aporte
                                print("Você manteve o valor da aposta.")
                        resultados.append(ValorSaldo)
                        print("Saldo atual: R$ ", ValorSaldo)
                        continuar = input("Deseja continuar? (s/n) ")
                        if continuar == "n":
                            print("Saindo...")
                            break
                        elif ValorSaldo < 10:
                            print("Saldo insuficiente")
                            break
                else:
                    print("Saindo...")
                    break
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
        plt.plot(resultados, marker='o')
        plt.title('Desempenho das Apostas no Fortune Tiger')
        plt.xlabel('Jogadas')
        plt.ylabel('Saldo (R$)')
        plt.grid(True)
        plt.show()
        break
    elif opcao == 5:
        with open('resultados.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if os.path.getsize('resultados.csv') == 0:
                writer.writerow(['Jogada', 'Saldo'])
            for i, saldo in enumerate(resultados[-jogadas:]):
                writer.writerow([i + 1, saldo])
        print("Resultados exportados para resultados.csv")
    elif opcao == 6:
        plt.plot(resultados, marker='o')
        plt.title('Desempenho das Apostas no Fortune Tiger')
        plt.xlabel('Jogadas')
        plt.ylabel('Saldo (R$)')
        plt.grid(True)
        plt.show()
    else:
        print("Opção inválida")

print("Fim do programa")
print("=" * 40)
