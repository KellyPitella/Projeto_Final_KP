# Importações necessárias
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


def adicionar_notas():
  
    try:
        listar_alunos()
        aluno_idx = int(input("Digite o número do aluno: ")) - 1
        if 0 <= aluno_idx < len(alunos):
            aluno = alunos[aluno_idx]
            disciplina = input("Digite o nome da disciplina: ")
            notas = []

            for trimestre in range(1, 5):
                while True:
                    try:
                        nota = float(input(f"Digite a nota do {trimestre}º trimestre: "))
                        if 0 <= nota <= 100:
                            notas.append(nota)
                            break
                        else:
                            print("Nota deve estar entre 0 e 100.")
                    except ValueError:
                        print("Por favor, insira um número válido.")

            aprovado = all(nota >= 60 for nota in notas)
            status = "Aprovado" if aprovado else "Reprovado"

            if "notas" not in aluno:
                aluno["notas"] = []
            aluno["notas"].append({"disciplina": disciplina, "notas": notas, "status": status})
            print(f"Notas adicionadas com sucesso! Status do aluno: {status}")
        else:
            print("Número de aluno inválido.")
    except ValueError:
        print("Erro: as notas devem ser números válidos.")

def listar_notas():

    if not alunos or all("notas" not in aluno for aluno in alunos):
        print("Nenhuma nota cadastrada.")
    else:
        print("Lista de Notas:")
        for aluno in alunos:
            if "notas" in aluno:
                for nota in aluno["notas"]:
                    print(f"Aluno: {aluno['nome']} - Disciplina: {nota['disciplina']} - Notas: {nota['notas']} - Status: {nota['status']}")
