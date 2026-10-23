# Diário de Desenvolvimento — Ordenação Inteligente

## Identificação do projeto

**Projeto:** Ordenação Inteligente  
**Objetivo:** Desenvolver um programa que analisa uma lista e escolhe um algoritmo de ordenação com base em suas características.

## Registro 1 — Planejamento

**Objetivo da etapa:** Definir os componentes do projeto e os algoritmos que serão comparados.

Foram definidos seis métodos de ordenação: Inserção, Intercalação (Merge Sort), Quick Sort com pivô aleatório, algoritmo híbrido, Contagem (Counting Sort) e Base (Radix Sort).

Também foram planejados quatro cenários de experimentação: dados aleatórios com chaves grandes, faixa de valores estreita, lista quase ordenada e lista minúscula.

## Registro 2 — Implementação dos algoritmos

**Objetivo da etapa:** Implementar os seis algoritmos em Python.

Os métodos foram organizados no arquivo `ordenacoes.py`. Foram criados testes para verificar listas vazias, listas com um elemento, valores repetidos, listas ordenadas, listas em ordem inversa e números negativos.

**Resultado:** Os testes iniciais dos seis algoritmos foram executados com sucesso.

## Registro 3 — Implementação do seletor

**Objetivo da etapa:** Criar as funções `escolher(v)` e `ordenar(v)`.

A função `escolher(v)` analisa características da lista e seleciona um método. A função `ordenar(v)` executa o método selecionado e devolve a lista ordenada e o nome do método.

**Observação:** As regras de seleção são heurísticas e podem escolher um método que não seja o mais rápido para determinada entrada.

## Registro 4 — Primeiros experimentos

**Objetivo da etapa:** Medir os seis algoritmos fixos e o seletor nos quatro cenários definidos.

Foi criado o arquivo `experimentos.py`, que mede tempos de execução, verifica a ordenação produzida e grava os resultados em `resultados.csv`.

Durante o primeiro experimento, a Contagem tentou processar uma faixa numérica muito grande, causando uma execução excessivamente demorada. O experimento foi interrompido e recebeu uma verificação de limite para evitar essa situação.

**Observação:** A Contagem foi ignorada no cenário em que a faixa de valores ultrapassou 100.000 posições. Esse comportamento precisa ser considerado na interpretação dos resultados.

## Registro 5 — Visualização dos resultados

**Objetivo da etapa:** Facilitar a comparação dos tempos medidos.

Foi criado o arquivo `graficos.py` para gerar gráficos de barras a partir do CSV dos experimentos.

Os gráficos permitem observar as diferenças de desempenho entre os algoritmos em cada cenário.

## Próximos registros

- Melhorar a medição do custo de seleção.
- Validar a metodologia e repetir os experimentos finais.
- Analisar os resultados e identificar casos em que o seletor perde.
- Elaborar o relatório técnico.
- Documentar a instalação e a reprodução dos experimentos no README.
- Conferir os arquivos e publicar a versão final no GitHub.