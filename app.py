from flask import Flask, render_template, request, redirect, url_for, jsonify
import tigrin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    saldo = float(request.form['saldo'])
    tigrin.start_game(saldo)
    return '', 204  # No Content

@app.route('/play_fortune_tiger', methods=['POST'])
def play_fortune_tiger():
    aporte = float(request.json['aporte'])
    resultado = tigrin.play_fortune_tiger(aporte)
    saldo = tigrin.get_saldo()
    return jsonify({'resultado': resultado, 'saldo': saldo})

if __name__ == '__main__':
    app.run(debug=True)