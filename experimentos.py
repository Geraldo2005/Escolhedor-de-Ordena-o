import csv
import random
import statistics
import time

from ordenacoes import (
    insercao,
    intercala,
    rapida,
    hibrida,
    contagem,
    base,
)

from seletor import escolher


# ============================================================
# CONFIGURAÇÕES
# ============================================================

METODOS = {
    "Inserção": insercao,
    "Intercalação": intercala,
    "Quick Sort aleatório": rapida,
    "Híbrida": hibrida,
    "Contagem": contagem,
    "Radix Sort": base,
}

REPETICOES = 10
TAMANHO = 2000

# Evita executar Counting Sort em faixas excessivamente grandes.
LIMITE_CONTAGEM = 100_000


# ============================================================
# GERAÇÃO DOS CENÁRIOS
# ============================================================

def gerar_cenarios():
    aleatorio = random.Random(42)

    # Cenário 1: números aleatórios com chaves grandes.
    lista_grande = [
        aleatorio.randint(-10**9, 10**9)
        for _ in range(TAMANHO)
    ]

    # Cenário 2: números concentrados em uma faixa pequena.
    faixa_estreita = [
        aleatorio.randint(-100, 100)
        for _ in range(TAMANHO)
    ]

    # Cenário 3: lista quase ordenada.
    quase_ordenada = list(range(TAMANHO))

    for _ in range(max(1, TAMANHO // 100)):
        i = aleatorio.randrange(TAMANHO)
        j = aleatorio.randrange(TAMANHO)

        quase_ordenada[i], quase_ordenada[j] = (
            quase_ordenada[j],
            quase_ordenada[i],
        )

    # Cenário 4: lista pequena.
    lista_minuscula = [
        aleatorio.randint(-1000, 1000)
        for _ in range(20)
    ]

    return {
        "Aleatório com chaves grandes": lista_grande,
        "Faixa estreita": faixa_estreita,
        "Quase ordenado": quase_ordenada,
        "Lista minúscula": lista_minuscula,
    }


# ============================================================
# MEDIÇÃO DE UM ALGORITMO FIXO
# ============================================================

def medir(metodo, entrada, esperado):
    inicio = time.perf_counter()

    resultado = metodo(entrada)

    fim = time.perf_counter()

    # A validação ocorre fora do intervalo cronometrado.
    if resultado != esperado:
        raise AssertionError(
            f"{metodo.__name__} produziu uma ordenação incorreta."
        )

    return fim - inicio


# ============================================================
# MEDIÇÃO DO SELETOR INTELIGENTE
# ============================================================

def medir_seletor(entrada, esperado):
    """
    Mede separadamente:
    - tempo para escolher o algoritmo;
    - tempo para executar o algoritmo escolhido;
    - tempo total, incluindo a escolha.
    """

    tempos_selecao = []
    tempos_ordenacao = []
    tempos_totais = []
    metodos_escolhidos = []

    for _ in range(REPETICOES):
        copia = entrada.copy()

        # O tempo total começa antes da escolha.
        inicio_total = time.perf_counter()

        # Mede somente a escolha.
        inicio = time.perf_counter()
        nome_escolhido, _ = escolher(copia)
        fim = time.perf_counter()

        tempo_selecao = fim - inicio

        if nome_escolhido not in METODOS:
            raise ValueError(
                f"Algoritmo desconhecido: {nome_escolhido}"
            )

        # Mede somente a ordenação.
        inicio = time.perf_counter()
        resultado = METODOS[nome_escolhido](copia)
        fim = time.perf_counter()

        tempo_ordenacao = fim - inicio

        # O tempo total termina depois da ordenação.
        fim_total = time.perf_counter()

        if resultado != esperado:
            raise AssertionError(
                "O seletor produziu uma ordenação incorreta."
            )

        tempos_selecao.append(tempo_selecao)
        tempos_ordenacao.append(tempo_ordenacao)
        tempos_totais.append(fim_total - inicio_total)
        metodos_escolhidos.append(nome_escolhido)

    return {
        "tempo_selecao_ms": (
            statistics.median(tempos_selecao) * 1000
        ),
        "tempo_ordenacao_ms": (
            statistics.median(tempos_ordenacao) * 1000
        ),
        "tempo_total_ms": (
            statistics.median(tempos_totais) * 1000
        ),
        "metodo_escolhido": statistics.mode(metodos_escolhidos),
    }


# ============================================================
# EXECUÇÃO DOS EXPERIMENTOS
# ============================================================

def executar_experimentos():
    cenarios = gerar_cenarios()
    resultados = []

    for nome_cenario, entrada in cenarios.items():
        print("\n" + "=" * 60)
        print(f"Cenário: {nome_cenario}")
        print(f"Tamanho: {len(entrada)} elementos")
        print("=" * 60)

        # Referência para validar todas as ordenações.
        esperado = sorted(entrada)

        # ----------------------------------------------------
        # Testa cada algoritmo fixo.
        # ----------------------------------------------------

        for nome_metodo, metodo in METODOS.items():

            # Proteção para não tentar criar uma contagem
            # gigantesca no Counting Sort.
            if nome_metodo == "Contagem" and entrada:
                faixa = max(entrada) - min(entrada) + 1

                if faixa > LIMITE_CONTAGEM:
                    print(
                        f"{nome_metodo}: ignorado neste cenário "
                        f"(faixa de {faixa:,} valores; "
                        f"limite de {LIMITE_CONTAGEM:,})"
                    )

                    resultados.append({
                        "cenario": nome_cenario,
                        "metodo": nome_metodo,
                        "tamanho": len(entrada),
                        "tempo_mediano_ms": "",
                        "repeticoes": 0,
                        "tempo_selecao_ms": "",
                        "tempo_ordenacao_ms": "",
                        "metodo_escolhido": "",
                        "status": "Ignorado: faixa excessiva",
                    })

                    continue

            tempos = []

            for _ in range(REPETICOES):
                tempo = medir(
                    metodo,
                    entrada.copy(),
                    esperado,
                )
                tempos.append(tempo)

            tempo_mediano = statistics.median(tempos) * 1000

            resultados.append({
                "cenario": nome_cenario,
                "metodo": nome_metodo,
                "tamanho": len(entrada),
                "tempo_mediano_ms": tempo_mediano,
                "repeticoes": REPETICOES,
                "tempo_selecao_ms": "",
                "tempo_ordenacao_ms": "",
                "metodo_escolhido": "",
                "status": "Executado",
            })

            print(f"{nome_metodo}: {tempo_mediano:.4f} ms")

        # ----------------------------------------------------
        # Testa o seletor inteligente.
        # ----------------------------------------------------

        dados_seletor = medir_seletor(entrada, esperado)

        resultados.append({
            "cenario": nome_cenario,
            "metodo": "Seletor inteligente",
            "tamanho": len(entrada),
            "tempo_mediano_ms": dados_seletor["tempo_total_ms"],
            "repeticoes": REPETICOES,
            "tempo_selecao_ms": dados_seletor["tempo_selecao_ms"],
            "tempo_ordenacao_ms": dados_seletor["tempo_ordenacao_ms"],
            "metodo_escolhido": dados_seletor["metodo_escolhido"],
            "status": "Executado",
        })

        print("\nSeletor inteligente:")
        print(
            f"  Tempo de seleção: "
            f"{dados_seletor['tempo_selecao_ms']:.4f} ms"
        )
        print(
            f"  Tempo de ordenação: "
            f"{dados_seletor['tempo_ordenacao_ms']:.4f} ms"
        )
        print(
            f"  Tempo total: "
            f"{dados_seletor['tempo_total_ms']:.4f} ms"
        )
        print(
            f"  Método escolhido: "
            f"{dados_seletor['metodo_escolhido']}"
        )

    # ========================================================
    # SALVAR RESULTADOS NO CSV
    # ========================================================

    campos = [
        "cenario",
        "metodo",
        "tamanho",
        "tempo_mediano_ms",
        "repeticoes",
        "tempo_selecao_ms",
        "tempo_ordenacao_ms",
        "metodo_escolhido",
        "status",
    ]

    with open(
        "resultados.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos,
        )

        escritor.writeheader()
        escritor.writerows(resultados)

    print("\n" + "=" * 60)
    print("Experimentos concluídos.")
    print("Resultados salvos em resultados.csv")
    print(f"Total de registros: {len(resultados)}")
    print("=" * 60)


if __name__ == "__main__":
    executar_experimentos()
