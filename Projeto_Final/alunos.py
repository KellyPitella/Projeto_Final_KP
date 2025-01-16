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
            "disciplinas": disciplinas,
            "notas": {}
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
            disciplinas_formatadas = ', '.join(aluno['disciplinas'])
            print(f"{idx}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Ano Escolar: {aluno['ano_escolar']}, Disciplinas: {disciplinas_formatadas}")
            
def adicionar_notas():
    if not alunos:
        print("Nenhum aluno cadastrado para adicionar notas.")
        return

    try:
        listar_alunos()
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
    if not alunos or all(not aluno['notas'] for aluno in alunos):
        print("Nenhuma nota cadastrada.")
    else:
        print("Lista de Notas:")
        for aluno in alunos:
            if aluno['notas']:
                print(f"Aluno: {aluno['nome']}")
                for disciplina, info in aluno['notas'].items():
                    notas_formatadas = ', '.join(map(str, info['notas']))
                    print(f"  Disciplina: {disciplina} - Notas: {notas_formatadas} - Status: {info['status']}")            