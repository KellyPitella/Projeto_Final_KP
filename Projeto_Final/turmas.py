from professores import listar_professores
from alunos import listar_alunos

def criar_turma(turmas, professores, alunos):
    try:
        nome_turma = input("Digite o nome da turma: ")
        
        listar_professores(professores)
        professor_idx = int(input("Digite o número do professor responsável: ")) - 1
        
        if 0 <= professor_idx < len(professores):
            professor_responsavel = professores[professor_idx]
            
            if alunos:
                listar_alunos(alunos)
                alunos_associados = []
                
                while True:
                    aluno_idx = input("Digite o número do aluno para associar à turma (ou pressione Enter para finalizar): ")
                    if not aluno_idx:
                        break
                    try:
                        aluno_idx = int(aluno_idx) - 1
                        if 0 <= aluno_idx < len(alunos):
                            alunos_associados.append(alunos[aluno_idx])
                        else:
                            print("Aluno inválido. Escolha um número válido.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
                
                turmas.append({
                    "nome": nome_turma,
                    "professor": professor_responsavel,
                    "alunos": alunos_associados
                })
                print(f"Turma {nome_turma} criada com sucesso!")
            else:
                print("Nenhum aluno cadastrado. Não é possível associar alunos à turma.")
        else:
            print("Número de professor inválido.")
    
    except ValueError:
        print("Erro: O número do professor deve ser um número inteiro.")

def listar_turmas(turmas):
    if not turmas:
        print("Nenhuma turma cadastrada.")
    else:
        print("\n--- Lista de Turmas ---")
        for idx, turma in enumerate(turmas, start=1):
            print(f"{idx}. Nome da Turma: {turma['nome']}")
            print(f"   Professor Responsável: {turma['professor']['nome']}")
            if turma.get('alunos'):
                print("   Alunos:")
                for aluno in turma['alunos']:
                    print(f"     - {aluno['nome']} (Ano Escolar: {aluno['ano_escolar']})")
            else:
                print("   Nenhum aluno associado à turma.")