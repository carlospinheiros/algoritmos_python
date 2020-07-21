# Algoritmo que implementa um menu.


def op_1():
    return "um!"


def op_2():
    return "dois!"


def op_3():
    return "três!"


def op_4():
    return "quatro!"


switcher = {
    str(1): op_1,
    str(2): op_2,
    str(3): op_3,
    str(4): op_4
}


def funcao(op):
    # Obter a função com as opções
    retorno = switcher.get(op, "Opção inválida!")
    while retorno == "Opção inválida!":
        print("Opção inválida!")
        print('=-=-=- MENU OPÇÕES -=-=-=''''
            [1] um
            [2] dois
            [3] tres
            [4] quatro''')
        nova_op = str(input(">>>> Para continuar escolha uma das opções acima: "))
        retorno = switcher.get(nova_op, "Opção inválida!")

    return retorno()  # Executa a função


# -------------------------------
# Main
# -------------------------------


if __name__ == "__main__":
    print('=-=-=-=- MENU OPÇÕES -=-=-=-=''''
        [1] um
        [2] dois
        [3] três
        [4] quatro''')
    opcao = str(input('>>>> Escolha uma opção: '))
    print(funcao(opcao))
