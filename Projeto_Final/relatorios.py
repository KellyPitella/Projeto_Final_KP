from fpdf import FPDF
import openpyxl

def salvar_em_pdf(alunos, professores, turmas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Gestão Escolar", ln=True, align="C")
    pdf.ln(10)

    # Adicionar dados de alunos
    pdf.cell(200, 10, txt="--- Alunos ---", ln=True)
    if alunos:
        for aluno in alunos:
            pdf.cell(200, 10, txt=f"Nome: {aluno['nome']}, Ano Escolar: {aluno['ano_escolar']}", ln=True)
    else:
        pdf.cell(200, 10, txt="Nenhum aluno cadastrado.", ln=True)

    # Adicionar dados de professores
    pdf.cell(200, 10, txt="--- Professores ---", ln=True)
    if professores:
        for professor in professores:
            pdf.cell(200, 10, txt=f"Nome: {professor['nome']}, Especialidade: {', '.join(professor['especialidade'])}", ln=True)
    else:
        pdf.cell(200, 10, txt="Nenhum professor cadastrado.", ln=True)

    pdf.output("Relatorio_Gestao_Escolar.pdf")
    print("Relatório salvo em PDF.")

def salvar_em_excel(alunos, professores, turmas):
    wb = openpyxl.Workbook()
    ws_alunos = wb.active
    ws_alunos.title = "Alunos"
    ws_alunos.append(["Nome", "Idade", "Ano Escolar"])
    for aluno in alunos:
        ws_alunos.append([aluno['nome'], aluno['idade'], aluno['ano_escolar']])

    ws_professores = wb.create_sheet("Professores")
    ws_professores.append(["Nome", "Especialidade"])
    for professor in professores:
        ws_professores.append([professor['nome'], ', '.join(professor['especialidade'])])

    wb.save("Relatorio_Gestao_Escolar.xlsx")
    print("Relatório salvo em Excel.")