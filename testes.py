
from ordenacoes import (
    insercao,
    intercala,
    rapida,
    hibrida,
    contagem,
    base,
)


METODOS = {
    "Inserção": insercao,
    "Intercalação": intercala,
    "Quick Sort aleatório": rapida,
    "Híbrida": hibrida,
    "Contagem": contagem,
    "Radix Sort": base,
}


CASOS = [
    [],
    [7],
    [5, 5, 5, 5],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-8, -3, -10, 0, 4, -3],
    [12, -5, 7, 12, 0, -20, 3],
]


def executar_testes():
    for nome, metodo in METODOS.items():
        for entrada in CASOS:
            original = entrada.copy()
            esperado = sorted(entrada)
            obtido = metodo(entrada)

            assert obtido == esperado, (
                f"{nome} falhou: entrada={entrada}, "
                f"esperado={esperado}, obtido={obtido}"
            )

            assert entrada == original, (
                f"{nome} modificou a lista original: {entrada}"
            )

        print(f"[OK] {nome}: todos os testes passaram.")


from seletor import escolher, ordenar


def testar_seletor():
    casos = [
        [],
        [5],
        [4, 2, 3, 1],
        list(range(100)),
        [7] * 100,
        list(range(100, 0, -1)),
        [1000000, -500000, 700000, 0] * 30,
    ]

    for entrada in casos:
        esperado = sorted(entrada)
        resultado, metodo = ordenar(entrada)

        assert resultado == esperado, (
            f"Seletor falhou com {entrada[:10]}"
        )

        nome, dados = escolher(entrada)

        assert nome == metodo
        assert dados["tamanho"] == len(entrada)

        print(
            f"[OK] tamanho={len(entrada)}, "
            f"método={metodo}"
        )


if __name__ == "__main__":
    executar_testes()
    testar_seletor()