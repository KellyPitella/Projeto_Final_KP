professores = []

def cadastrar_professor():
    try:
        nome = input("Digite o nome do professor: ")
        especialidade = input("Digite a especialidade (disciplinas que leciona, separadas por vírgula): ").split(',')
        horarios = input("Digite os horários disponíveis (separados por vírgula): ").split(',')

        professores.append({"nome": nome, "especialidade": especialidade, "horarios": horarios})
        print(f"Professor {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar professor: {e}")

def listar_professores():
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        print("Lista de Professores:")
        for idx, professor in enumerate(professores, start=1):
            print(f"{idx}. {professor['nome']} - Especialidade: {', '.join(professor['especialidade'])}")