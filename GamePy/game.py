from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos, dificuldade())


def jogar(pontos: int, nivel: int) -> None:
    calc: Calcular = Calcular(nivel)

    calc.mostrar_operacao()

    resposta: int = int(input())
    if calc.checar_resultado(resposta):
        pontos += 1
        print(f'Resposta correta! +1 Ponto ({pontos} total)')
    else:
        print(f'Resposta errada, o resultado era {calc.resultado}')

    continuar: int = int(input('Deseja continuar?[1-Sim 2-Não]\n'))
    if continuar == 1:
        jogar(pontos, nivel)
    else:
        print(f'Pontuação Final: {pontos}!')


def dificuldade() -> int:
    nivel: int = int(input('Informe o nível de dificuldade:\n1: Fácil\n2: Médio\n3: Difícil\n'))
    return nivel


if __name__ == '__main__':
    main()
