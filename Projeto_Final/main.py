import json
from alunos import listar_alunos, cadastrar_aluno, adicionar_notas, listar_notas
from professores import listar_professores, cadastrar_professor
from turmas import criar_turma, listar_turmas
from relatorios import salvar_em_pdf, salvar_em_excel

# Inicialização das listas globais
alunos = []
professores = []
turmas = []

def salvar_dados(alunos, professores, turmas, arquivo="dados_escolares.json"):
    """Salva os dados em um arquivo JSON."""
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump({
                "alunos": alunos,
                "professores": professores,
                "turmas": turmas
            }, f, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados(arquivo="dados_escolares.json"):
    """Carrega os dados de um arquivo JSON."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            print("Dados carregados com sucesso!")
            return dados.get("alunos", []), dados.get("professores", []), dados.get("turmas", [])
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Iniciando com dados vazios.")
        return [], [], []
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return [], [], []

# Carrega os dados salvos ao iniciar o programa
alunos, professores, turmas = carregar_dados()

while True:
    print("\n--- Gestão de Secretaria Escolar ---")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Cadastrar Professor")
    print("4. Listar Professores")
    print("5. Criar Turma")
    print("6. Listar Turmas")
    print("7. Adicionar Notas a um Aluno")
    print("8. Listar Notas dos Alunos")
    print("9. Salvar Relatório em PDF")
    print("10. Salvar Relatório em Excel")
    print("11. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        cadastrar_professor()
    elif opcao == "4":
        listar_professores()
    elif opcao == "5":
        criar_turma()
    elif opcao == "6":
        listar_turmas()
    elif opcao == "7":
        adicionar_notas()
    elif opcao == "8":
        listar_notas()
    elif opcao == "9":
        salvar_em_pdf(alunos, professores, turmas)
    elif opcao == "10":
        salvar_em_excel(alunos, professores, turmas)
    elif opcao == "11":
        salvar_dados(alunos, professores, turmas)
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida.")