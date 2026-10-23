
from ordenacoes import (
    insercao,
    intercala,
    rapida,
    hibrida,
    contagem,
    base,
)


def analisar(v):
    """
    Calcula características básicas da lista.
    Retorna um dicionário com informações para a decisão.
    """
    n = len(v)

    if n == 0:
        return {
            "tamanho": 0,
            "minimo": None,
            "maximo": None,
            "faixa": 0,
            "descidas": 0,
            "quase_ordenada": True,
        }

    minimo = min(v)
    maximo = max(v)
    faixa = maximo - minimo + 1

    descidas = 0

    for i in range(1, n):
        if v[i] < v[i - 1]:
            descidas += 1

    proporcao_descidas = descidas / max(1, n - 1)

    return {
        "tamanho": n,
        "minimo": minimo,
        "maximo": maximo,
        "faixa": faixa,
        "descidas": descidas,
        "quase_ordenada": proporcao_descidas <= 0.05,
    }


def escolher(v):
    """
    Escolhe um algoritmo com base nas características da entrada.
    Retorna o nome do método e as informações da análise.
    """
    dados = analisar(v)
    n = dados["tamanho"]
    faixa = dados["faixa"]

    if n <= 32:
        return "Inserção", dados

    if faixa <= 2 * n and faixa <= 100_000:
        return "Contagem", dados

    if dados["quase_ordenada"]:
        return "Inserção", dados

    return "Híbrida", dados


def ordenar(v):
    """
    Seleciona e executa o método.
    Retorna a lista ordenada e o nome do método selecionado.
    """
    nome, _ = escolher(v)

    metodos = {
        "Inserção": insercao,
        "Intercalação": intercala,
        "Quick Sort aleatório": rapida,
        "Híbrida": hibrida,
        "Contagem": contagem,
        "Radix Sort": base,
    }

    resultado = metodos[nome](v)

    return resultado, nome
