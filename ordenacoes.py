
import random


def insercao(v):
    """Ordena por inserção: eficiente para listas pequenas ou quase ordenadas."""
    resultado = v.copy()

    for i in range(1, len(resultado)):
        atual = resultado[i]
        j = i - 1

        while j >= 0 and resultado[j] > atual:
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = atual

    return resultado


def intercala(v):
    """Ordena por intercalação (Merge Sort): divide e combina as partes ordenadas."""
    if len(v) <= 1:
        return v.copy()

    meio = len(v) // 2
    esquerda = intercala(v[:meio])
    direita = intercala(v[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def rapida(v):
    """Quick Sort com pivô aleatório e partição em três grupos."""
    resultado = v.copy()
    _rapida_recursiva(resultado, 0, len(resultado) - 1)
    return resultado


def _rapida_recursiva(v, inicio, fim):
    if inicio >= fim:
        return

    pivo = v[random.randint(inicio, fim)]
    menor = inicio
    atual = inicio
    maior = fim

    while atual <= maior:
        if v[atual] < pivo:
            v[menor], v[atual] = v[atual], v[menor]
            menor += 1
            atual += 1
        elif v[atual] > pivo:
            v[atual], v[maior] = v[maior], v[atual]
            maior -= 1
        else:
            atual += 1

    _rapida_recursiva(v, inicio, menor - 1)
    _rapida_recursiva(v, maior + 1, fim)


def hibrida(v):
    """Quick Sort híbrido: usa inserção nas partições pequenas."""
    resultado = v.copy()
    limite = 16
    _hibrida_recursiva(resultado, 0, len(resultado) - 1, limite)
    return resultado


def _hibrida_recursiva(v, inicio, fim, limite):
    if fim - inicio + 1 <= limite:
        _insercao_intervalo(v, inicio, fim)
        return

    pivo = v[random.randint(inicio, fim)]
    menor = inicio
    atual = inicio
    maior = fim

    while atual <= maior:
        if v[atual] < pivo:
            v[menor], v[atual] = v[atual], v[menor]
            menor += 1
            atual += 1
        elif v[atual] > pivo:
            v[atual], v[maior] = v[maior], v[atual]
            maior -= 1
        else:
            atual += 1

    _hibrida_recursiva(v, inicio, menor - 1, limite)
    _hibrida_recursiva(v, maior + 1, fim, limite)


def _insercao_intervalo(v, inicio, fim):
    for i in range(inicio + 1, fim + 1):
        atual = v[i]
        j = i - 1

        while j >= inicio and v[j] > atual:
            v[j + 1] = v[j]
            j -= 1

        v[j + 1] = atual


def contagem(v):
    """Counting Sort: adequado quando a faixa de valores é pequena."""
    if len(v) <= 1:
        return v.copy()

    menor = min(v)
    maior = max(v)
    faixa = maior - menor + 1

    contadores = [0] * faixa

    for valor in v:
        contadores[valor - menor] += 1

    resultado = []

    for indice, quantidade in enumerate(contadores):
        for _ in range(quantidade):
            resultado.append(indice + menor)

    return resultado


def base(v):
    """Radix Sort decimal para inteiros, incluindo valores negativos."""
    if len(v) <= 1:
        return v.copy()

    negativos = [-valor for valor in v if valor < 0]
    positivos = [valor for valor in v if valor >= 0]

    negativos = _radix_positivo(negativos)
    positivos = _radix_positivo(positivos)

    negativos = [-valor for valor in reversed(negativos)]

    return negativos + positivos


def _radix_positivo(v):
    if not v:
        return []

    resultado = v.copy()
    maior = max(resultado)
    expoente = 1

    while maior // expoente > 0:
        contadores = [0] * 10

        for valor in resultado:
            digito = (valor // expoente) % 10
            contadores[digito] += 1

        for i in range(1, 10):
            contadores[i] += contadores[i - 1]

        saida = [0] * len(resultado)

        for valor in reversed(resultado):
            digito = (valor // expoente) % 10
            contadores[digito] -= 1
            saida[contadores[digito]] = valor

        resultado = saida
        expoente *= 10

    return resultado
