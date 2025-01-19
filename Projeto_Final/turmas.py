from professores import listar_professores, professores
from alunos import listar_alunos, alunos


turmas = []

def criar_turma():
    try:
        nome_turma = input("Digite o nome da turma: ")
        listar_professores()
        professor_idx = int(input("Digite o número do professor responsável: ")) - 1
        if 0 <= professor_idx < len(professores):
            professor_responsavel = professores[professor_idx]
            turmas.append({"nome": nome_turma, "professor": professor_responsavel})
            print(f"Turma {nome_turma} criada com sucesso!")
        else:
            print("Número de professor inválido.")
    except ValueError:
        print("Erro: o número do professor deve ser um número inteiro.")

def listar_turmas():
    
    if not turmas:
        print("Nenhuma turma cadastrada.")
    else:
        print("Lista de Turmas:")
        for idx, turma in enumerate(turmas, start=1):
            print(f"{idx}. {turma['nome']} - Professor: {turma['professor']['nome']}")
