alunos = []
materias = []

def cadastrar_aluno():
    try:
        aluno = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        ano_escolar = input("Digite o ano escolar: ")
        disciplinas = input("Digite as disciplinas (separadas por vírgula): ").split(',')

        alunos.append({
            "nome": aluno,
            "idade": idade,
            "ano_escolar": ano_escolar,
            "disciplinas": disciplinas
        })
        print(f"Aluno {aluno} cadastrado com sucesso!")
    except ValueError:
        print("Erro: idade deve ser um número inteiro.")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for idx, aluno in enumerate(alunos, start=1):
            print(f"{idx}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Ano Escolar: {aluno['ano_escolar']}")