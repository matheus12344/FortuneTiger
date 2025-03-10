document.addEventListener('DOMContentLoaded', function() {
    const gameOptions = document.getElementById('gameOptions');
    const startGameForm = document.getElementById('startGameForm');
    const gameResult = document.getElementById('gameResult');
    const resultMessage = document.getElementById('resultMessage');
    const currentSaldo = document.getElementById('currentSaldo');

    startGameForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const saldo = document.getElementById('saldo').value;
        if (saldo && saldo > 0) {
            fetch('/start_game', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({ saldo: saldo })
            })
            .then(response => {
                if (response.ok) {
                    gameOptions.style.display = 'block';
                    gameResult.style.display = 'none';
                }
            });
        }
    });

    document.getElementById('fortuneTiger').addEventListener('click', function() {
        const aporte = prompt("Digite o valor do aporte:");
        if (aporte) {
            fetch('/play_fortune_tiger', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ aporte: parseFloat(aporte) })
            })
            .then(response => response.json())
            .then(data => {
                resultMessage.textContent = data.resultado;
                currentSaldo.textContent = `Saldo atual: R$ ${data.saldo}`;
                gameResult.style.display = 'block';
            });
        }
    });

    // Adicione event listeners para outras opções de jogo aqui
    document.getElementById('fogueteDaSorte').addEventListener('click', function() {
        alert('Foguete da Sorte selecionado');
        // Adicione a lógica para Foguete da Sorte aqui
    });

    document.getElementById('jokenpo').addEventListener('click', function() {
        alert('Jokenpo selecionado');
        // Adicione a lógica para Jokenpo aqui
    });

    document.getElementById('exportResults').addEventListener('click', function() {
        alert('Exportar Resultados selecionado');
        // Adicione a lógica para exportar resultados aqui
    });

    document.getElementById('compareResults').addEventListener('click', function() {
        alert('Comparar Resultados selecionado');
        // Adicione a lógica para comparar resultados aqui
    });

    document.getElementById('exitGame').addEventListener('click', function() {
        alert('Saindo do jogo');
        // Adicione a lógica para sair do jogo aqui
    });
});