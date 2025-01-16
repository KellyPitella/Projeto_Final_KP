from alunos import cadastrar_aluno, listar_alunos, adicionar_notas, listar_notas
from professores import cadastrar_professor, listar_professores
from turmas import criar_turma, listar_turmas
from relatorios import salvar_em_pdf, salvar_em_excel

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
        salvar_em_pdf()
    elif opcao == "10":
        salvar_em_excel()
    elif opcao == "11":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida.")