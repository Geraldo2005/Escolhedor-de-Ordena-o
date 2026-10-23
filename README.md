# Ordenação Inteligente

## Sobre o projeto

O projeto **Ordenação Inteligente** implementa seis algoritmos de ordenação e um seletor que analisa características da lista de entrada para escolher um método.

O objetivo é comparar o desempenho dos algoritmos em diferentes cenários e avaliar se a escolha automática consegue obter bons resultados considerando também o custo da análise.

## Algoritmos implementados

- **Inserção (Insertion Sort):** adequado para listas pequenas e entradas quase ordenadas.
- **Intercalação (Merge Sort):** utiliza a divisão da lista em partes menores e a combinação ordenada dessas partes.
- **Quick Sort aleatório:** utiliza um pivô aleatório para particionar os elementos.
- **Híbrida:** combina estratégias de ordenação para melhorar o desempenho em diferentes partes da lista.
- **Contagem (Counting Sort):** utiliza a contagem de ocorrências e é especialmente útil quando a faixa dos valores é pequena.
- **Base (Radix Sort):** ordena números considerando seus dígitos.

## Seletor inteligente

O seletor analisa características da lista, como tamanho, faixa numérica e quantidade de descidas entre elementos consecutivos.

Com base nessas informações, escolhe um dos seguintes métodos:

- Inserção;
- Contagem;
- Híbrida.

As regras são heurísticas e não garantem que o método selecionado seja sempre o mais rápido em todas as entradas.

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `ordenacoes.py` | Implementação dos algoritmos de ordenação. |
| `seletor.py` | Análise da lista e seleção do algoritmo. |
| `testes.py` | Testes de funcionamento dos algoritmos. |
| `experimentos.py` | Execução dos experimentos e medição dos tempos. |
| `resultados.csv` | Resultados dos experimentos. |
| `graficos.py` | Geração dos gráficos de comparação. |
| `RELATORIO.md` | Análise dos resultados e conclusões. |
| `DIARIO.md` | Registro das etapas de desenvolvimento. |

## Requisitos

- Python 3;
- Biblioteca `matplotlib`, utilizada para gerar os gráficos.

## Como executar

Os comandos abaixo devem ser executados no terminal, dentro da pasta do projeto.

### 1. Instalar a dependência dos gráficos

```bash
python -m pip install matplotlib
```

### 2. Executar os testes

```bash
python testes.py
```

### 3. Executar os experimentos

```bash
python experimentos.py
```

Esse comando executa os algoritmos nos cenários definidos e atualiza o arquivo `resultados.csv`.

### 4. Gerar os gráficos

```bash
python graficos.py
```

Os gráficos são salvos em arquivos PNG na pasta do projeto.

## Cenários avaliados

O projeto utiliza quatro cenários:

1. Lista aleatória com chaves grandes;
2. Lista com faixa numérica estreita;
3. Lista quase ordenada;
4. Lista minúscula.

Cada método é executado dez vezes, e a mediana dos tempos é utilizada na comparação.

A Contagem é ignorada quando a faixa numérica ultrapassa o limite definido no experimento.

## Resultados

Os resultados detalhados, incluindo os tempos medidos, a análise do seletor e as limitações observadas, estão disponíveis no arquivo [`RELATORIO.md`](RELATORIO.md).

## Observações

Os tempos dependem do ambiente de execução, do computador e das características dos dados. O seletor pode reduzir o tempo total em determinados conjuntos de testes, mas sua análise também possui um custo e não garante superioridade universal.

Este projeto foi desenvolvido com fins acadêmicos para estudar algoritmos de ordenação, análise de desempenho e seleção adaptativa de métodos.

