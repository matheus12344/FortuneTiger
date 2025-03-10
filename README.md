# FortuneTiger

FortuneTiger é um projeto desenvolvido para fins de estudo e análise de dados, focado em simulações de condições randômicas. Este projeto não deve ser utilizado para apostas reais ou qualquer atividade relacionada a jogos de azar.

## Descrição

O FortuneTiger é um simulador de apostas que permite ao usuário jogar diferentes jogos e acompanhar o desempenho das apostas ao longo do tempo. O projeto inclui funcionalidades para:

- Jogar diferentes tipos de jogos com base em condições randômicas.
- Exportar os resultados das apostas para um arquivo CSV.
- Visualizar o desempenho das apostas em gráficos.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `tigrin.py`: Script que implementa o simulador de apostas FortuneTiger.
- `resultados.csv`: Arquivo CSV que armazena os resultados das apostas.

## Funcionalidades

### Jogos Disponíveis

1. **Fortune Tiger**: Jogo principal onde o usuário pode fazer apostas e ganhar ou perder com base em condições randômicas.
2. **Foguete da Sorte**: Jogo secundário com regras simplificadas.
3. **Jokenpo**: Jogo de pedra, papel e tesoura.

### Exportação de Resultados

Os resultados das apostas podem ser exportados para um arquivo CSV (`resultados.csv`) para posterior análise.

### Visualização de Desempenho

O desempenho das apostas pode ser visualizado em gráficos utilizando a biblioteca `matplotlib`.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências necessárias:
    ```sh
    pip install matplotlib
    ```
3. Execute o script `tigrin.py`:
    ```sh
    python tigrin.py
    ```

## Observações

- Este projeto é apenas para fins de estudo e análise de dados.
- Não utilize este projeto para apostas reais ou qualquer atividade relacionada a jogos de azar.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
