import csv
import matplotlib.pyplot as plt


ARQUIVO_CSV = "resultados.csv"


def gerar_graficos():
    dados = {}

    # Ler os resultados dos experimentos.
    with open(
        ARQUIVO_CSV,
        "r",
        newline="",
        encoding="utf-8",
    ) as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            cenario = linha["cenario"]
            metodo = linha["metodo"]
            tempo = linha["tempo_mediano_ms"]

            # Ignorar métodos sem tempo medido.
            if not tempo or not tempo.strip():
                continue

            try:
                tempo = float(tempo)
            except ValueError:
                print(
                    f"Aviso: tempo inválido ignorado: "
                    f"{cenario} - {metodo}"
                )
                continue

            if cenario not in dados:
                dados[cenario] = {}

            dados[cenario][metodo] = tempo

    # Criar um gráfico para cada cenário.
    for indice, (cenario, metodos) in enumerate(dados.items(), start=1):
        nomes = list(metodos.keys())
        tempos = list(metodos.values())

        plt.figure(figsize=(11, 6))
        barras = plt.bar(nomes, tempos)

        plt.title(f"Comparação de tempos - {cenario}")
        plt.xlabel("Método de ordenação")
        plt.ylabel("Tempo mediano (ms)")
        plt.xticks(rotation=25, ha="right")

        # Mostrar o valor sobre cada barra.
        for barra, tempo in zip(barras, tempos):
            plt.text(
                barra.get_x() + barra.get_width() / 2,
                barra.get_height(),
                f"{tempo:.3f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        plt.tight_layout()

        nome_arquivo = f"grafico_cenario_{indice}.png"
        plt.savefig(nome_arquivo, dpi=150)
        plt.close()

        print(f"Gráfico salvo: {nome_arquivo}")

    print("\nGeração dos gráficos concluída.")


if __name__ == "__main__":
    gerar_graficos()