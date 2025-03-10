import random
import matplotlib.pyplot as plt
import csv
import os

ValorSaldo = 0
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

def start_game(saldo):
    global ValorSaldo, jogadas, resultados
    ValorSaldo = saldo
    jogadas = 0
    resultados = []
    load_results()

def play_fortune_tiger(aporte):
    global ValorSaldo, jogadas, resultados
    if aporte > ValorSaldo:
        return "Aporte maior que o saldo"
    elif aporte < 10:
        return "Aporte menor que o mínimo permitido"
    else:
        ValorSaldo -= aporte
        jogadas += 1
        if jogadas <= 3:
            ganho = random.choice([aporte*2, aporte*3])
            ValorSaldo += ganho
            resultado = f"Você ganhou R$ {ganho}!"
        else:
            resultado = random.choice(["ganhou", "perdeu", "neutro"])
            if resultado == "ganhou":
                ganho = random.choice([aporte, aporte*2])
                ValorSaldo += ganho
                resultado = f"Você ganhou R$ {ganho}!"
            elif resultado == "perdeu":
                resultado = "Você perdeu a aposta."
            else:
                ValorSaldo += aporte
                resultado = "Você manteve o valor da aposta."
        resultados.append(ValorSaldo)
        return resultado

def get_saldo():
    return ValorSaldo

def get_resultados():
    return resultados
