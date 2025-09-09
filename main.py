# Refatorar nosso código usando Dicionário, Type Hint e Funções.


def gerar_kpi_de_bonus() -> dict[str, float | str]:
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    # Solicita ao usuário que digite seu nome
    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")

            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)

    # Solicita ao usuário que digite o valor do seu salário
    while not salario_valido:
        try:
            salario: float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    # Solicita ao usuário que digite o valor do bônus recebido
    while not bonus_valido:
        try:
            bonus: float = float(input("Digite o valor do bônus recebido: "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    bonus_recebido: float = 1000 + salario * bonus

    # Monta o dicionário de resultado
    resultado: dict[str, float | str] = {
        "nome": nome,
        "salario": salario,
        "bonus": bonus,
        "bonus_final": bonus_recebido,
    }

    # Imprime as informações para o usuário
    print(
        f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}."
    )

    return resultado


# Chamada da função
print(gerar_kpi_de_bonus())
