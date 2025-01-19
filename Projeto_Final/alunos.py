import json

alunos = []
materias = []

def cadastrar_aluno(alunos):
    try:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        ano_escolar = int(input("Digite o ano escolar do aluno: "))
        disciplinas = input("Digite as disciplinas do aluno (separadas por vírgula): ").split(",")
        
        aluno = {
            "nome": nome,
            "idade": idade,
            "ano_escolar": ano_escolar,
            "disciplinas": [disciplina.strip() for disciplina in disciplinas],
            "notas": {}
        }
        
        alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: A idade e o ano escolar devem ser números inteiros.")


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for idx, aluno in enumerate(alunos, start=1):
            disciplinas = ', '.join(aluno['disciplinas'])
            print(f"{idx}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Ano Escolar: {aluno['ano_escolar']}, Disciplinas: {disciplinas}")
            
def adicionar_notas(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado para adicionar notas.")
        return

    try:
        listar_alunos(alunos)
        aluno_idx = int(input("Digite o número do aluno: ")) - 1
        if 0 <= aluno_idx < len(alunos):
            aluno = alunos[aluno_idx]
            disciplina = input("Digite o nome da disciplina: ").strip()
            
            if disciplina not in aluno['disciplinas']:
                print(f"Erro: A disciplina '{disciplina}' não está associada ao aluno.")
                return

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

            aluno['notas'][disciplina] = {"notas": notas, "status": status}
            print(f"Notas adicionadas com sucesso! Status do aluno em {disciplina}: {status}")
        else:
            print("Número de aluno inválido.")
    except ValueError:
        print("Erro: As entradas devem ser números válidos.")
        
def listar_notas():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Aluno: {aluno['nome']}")
            for disciplina, info in aluno['notas'].items():
                notas = ', '.join(map(str, info['notas']))
                print(f"  Disciplina: {disciplina} - Notas: {notas} - Status: {info['status']}")        