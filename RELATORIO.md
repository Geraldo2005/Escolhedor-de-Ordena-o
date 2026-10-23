# Relatório — Ordenação Inteligente

## 1. Objetivo

O objetivo deste projeto é implementar diferentes algoritmos de ordenação e desenvolver um seletor inteligente capaz de escolher um método com base nas características da lista de entrada.

Foram implementados seis algoritmos: Inserção, Intercalação (Merge Sort), Quick Sort aleatório, Híbrida, Contagem (Counting Sort) e Radix Sort.

O desempenho foi avaliado em quatro cenários diferentes, comparando os métodos individualmente com o seletor inteligente. Cada método foi executado dez vezes, e a mediana dos tempos foi utilizada para reduzir a influência de variações pontuais nas medições.

## 2. Metodologia

Os experimentos foram executados em Python, utilizando `time.perf_counter()` para medir os tempos de execução.

Foram utilizados os seguintes cenários:

- **Aleatório com chaves grandes:** 2.000 números inteiros aleatórios entre -1.000.000.000 e 1.000.000.000.
- **Faixa estreita:** 2.000 números inteiros aleatórios entre -100 e 100.
- **Quase ordenado:** lista inicialmente ordenada de 2.000 elementos, com trocas aleatórias em aproximadamente 1% das posições.
- **Lista minúscula:** lista de 20 números inteiros aleatórios entre -1.000 e 1.000.

Os tempos apresentados são medianas de dez execuções, em milissegundos (ms). Os resultados dependem do computador, do ambiente de execução e das entradas utilizadas.

## 3. Resultados dos experimentos

### 3.1. Aleatório com chaves grandes

| Método | Tempo mediano (ms) |
|---|---:|
| Inserção | 57,5939 |
| Intercalação | 2,6087 |
| Quick Sort aleatório | 2,5562 |
| Híbrida | 2,1292 |
| Contagem | Não executado |
| Radix Sort | 2,4543 |
| Seletor inteligente | 2,2028 |

O método Híbrido apresentou o menor tempo entre os algoritmos fixos executados. O Counting Sort foi ignorado porque a faixa numérica excedeu o limite de 100.000 definido no experimento.

O seletor escolheu o método Híbrido e obteve um tempo total próximo ao melhor resultado fixo.

### 3.2. Faixa estreita

| Método | Tempo mediano (ms) |
|---|---:|
| Inserção | 55,1102 |
| Intercalação | 2,6569 |
| Quick Sort aleatório | 1,3458 |
| Híbrida | 1,3973 |
| Contagem | 0,1788 |
| Radix Sort | 0,8745 |
| Seletor inteligente | 0,3473 |

O Counting Sort foi o método mais rápido nesse cenário. Isso ocorre porque os valores estão concentrados em uma faixa pequena, tornando viável contar as ocorrências dos números e reconstruir a lista ordenada.

O seletor identificou essa característica e escolheu Contagem. O tempo total do seletor foi maior que o do Counting Sort executado diretamente, pois também inclui o custo da análise da entrada.

### 3.3. Quase ordenado

| Método | Tempo mediano (ms) |
|---|---:|
| Inserção | 1,0247 |
| Intercalação | 2,0672 |
| Quick Sort aleatório | 2,3754 |
| Híbrida | 2,0658 |
| Contagem | 0,3378 |
| Radix Sort | 1,0509 |
| Seletor inteligente | 0,4152 |

O Counting Sort apresentou o menor tempo neste experimento, seguido pela Inserção. Embora a lista estivesse quase ordenada, a faixa numérica continuou pequena o suficiente para favorecer o Counting Sort.

O seletor escolheu Contagem porque sua regra de faixa numérica é verificada antes da regra de quase ordenação.

### 3.4. Lista minúscula

| Método | Tempo mediano (ms) |
|---|---:|
| Inserção | 0,0060 |
| Intercalação | 0,0135 |
| Quick Sort aleatório | 0,0105 |
| Híbrida | 0,0067 |
| Contagem | 0,1212 |
| Radix Sort | 0,0143 |
| Seletor inteligente | 0,0085 |

A Inserção foi o método mais rápido para a lista minúscula. Para entradas pequenas, o baixo custo de implementação e execução do algoritmo pode compensar sua complexidade quadrática no pior caso.

O seletor escolheu Inserção, conforme a regra definida para listas com até 32 elementos.

## 4. Regras do seletor inteligente

O seletor está implementado no arquivo `seletor.py`. A função `analisar(v)` calcula características da entrada, incluindo tamanho, valor mínimo, valor máximo, faixa numérica e quantidade de descidas entre elementos consecutivos.

A função `escolher(v)` utiliza as seguintes regras, na ordem apresentada:

1. Se a lista tiver até 32 elementos, escolher Inserção.
2. Se a faixa numérica for menor ou igual a duas vezes o tamanho da lista e não ultrapassar 100.000, escolher Contagem.
3. Se a proporção de descidas consecutivas for menor ou igual a 5%, escolher Inserção.
4. Nos demais casos, escolher Híbrida.

A função `ordenar(v)` seleciona o método e executa o algoritmo correspondente.

### 4.1. Origem das regras

Os limites de 32 elementos, 100.000 valores de faixa e 5% de descidas são parâmetros definidos na implementação do projeto. Eles representam critérios heurísticos, e não limites universais que garantem o melhor desempenho em qualquer computador ou conjunto de dados.

A escolha de Contagem considera que seu custo depende tanto do número de elementos quanto da amplitude dos valores. A escolha de Inserção para listas pequenas busca evitar custos adicionais de algoritmos mais complexos.

### 4.2. Limitações das regras

O seletor não escolhe diretamente Intercalação, Quick Sort aleatório ou Radix Sort, embora esses algoritmos sejam implementados e avaliados nos experimentos.

Além disso, como a regra de faixa numérica aparece antes da regra de quase ordenação, uma lista quase ordenada com valores concentrados pode ser encaminhada para Contagem. Isso não é necessariamente um erro: nos dados medidos, Contagem foi mais rápido que os demais métodos nesse cenário.

## 5. Custo da seleção

A análise da entrada também consome tempo. A função `analisar(v)` calcula mínimo e máximo e percorre a lista para contar descidas consecutivas. Essas operações exigem tempo linear, O(n), no tamanho da lista.

No experimento, o tempo mediano de seleção e o tempo mediano de ordenação do método escolhido foram medidos separadamente.

| Cenário | Seleção (ms) | Ordenação (ms) | Total do seletor (ms) |
|---|---:|---:|---:|
| Aleatório com chaves grandes | 0,1166 | 2,0848 | 2,2028 |
| Faixa estreita | 0,1405 | 0,1970 | 0,3473 |
| Quase ordenado | 0,1003 | 0,3139 | 0,4152 |
| Lista minúscula | 0,0016 | 0,0066 | 0,0085 |

Os tempos individuais são medianas calculadas separadamente; por isso, a soma das medianas de seleção e ordenação pode diferir ligeiramente da mediana do tempo total.

O custo de seleção é especialmente relevante quando a ordenação é muito rápida, como nas listas pequenas. Ainda assim, a análise pode ser vantajosa quando evita um algoritmo inadequado para entradas grandes ou com faixa numérica excessiva.

## 6. Comparação geral

Somando as medianas dos quatro cenários, os resultados foram:

| Método | Soma das medianas (ms) |
|---|---:|
| Inserção | 113,7348 |
| Intercalação | 7,3462 |
| Quick Sort aleatório | 6,2879 |
| Híbrida | 5,5990 |
| Radix Sort | 4,3941 |
| Seletor inteligente | 2,9738 |

O Counting Sort não pode ser comparado nessa soma como se tivesse executado todos os cenários, pois foi ignorado no cenário de chaves grandes.

A soma indica que o seletor apresentou o menor total entre os métodos que foram executados nos quatro cenários. Entretanto, essa comparação é apenas uma visão agregada do conjunto de testes: os cenários possuem tamanhos e características diferentes, e o seletor não foi o método mais rápido em todos eles.

Para avaliar a qualidade da seleção, é importante observar tanto o resultado agregado quanto o desempenho individual de cada cenário.

## 7. Um caso em que o seletor pode não ser a melhor escolha

Na lista minúscula, a Inserção executada diretamente apresentou mediana de 0,0060 ms, enquanto o seletor levou 0,0085 ms no total.

A diferença é pequena em termos absolutos, mas demonstra que analisar a entrada antes de ordenar pode tornar a execução mais lenta quando a lista é muito pequena.

Outro caso é o cenário de faixa estreita: o seletor escolheu corretamente Contagem, mas seu tempo total foi de 0,3473 ms, enquanto a execução direta de Contagem levou 0,1788 ms.

Esses exemplos demonstram que escolher um algoritmo adequado não elimina o custo da decisão.

## 8. Conclusão

Os experimentos demonstraram que diferentes algoritmos apresentam desempenhos distintos conforme o tamanho da entrada e a distribuição dos valores.

A Inserção foi adequada para a lista minúscula; o Counting Sort destacou-se nas entradas de faixa estreita e quase ordenadas; e o método Híbrido apresentou o melhor resultado fixo para a lista aleatória com chaves grandes.

O seletor inteligente adaptou sua escolha às características observadas e apresentou o menor somatório de medianas entre os métodos executados nos quatro cenários. Entretanto, a análise também acrescentou custo de execução, especialmente quando o algoritmo selecionado já era muito rápido.

Conclui-se que a seleção adaptativa pode ser útil, mas suas regras precisam ser avaliadas com diferentes entradas e ambientes. Os resultados obtidos são válidos para os experimentos realizados e não garantem superioridade universal sobre todos os algoritmos fixos.
