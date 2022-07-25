import sqlite3
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

fileName = 'relatorio.pdf'
documentTitle = 'relatorio'
subTitle = 'Relatorio folha de pagamento'

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)
pdf.setFont("Helvetica", 18)
pdf.setFillColorRGB(0, 0, 0)
pdf.drawCentredString(290, 720, subTitle)

pdf.line(30, 710, 550, 710)


banco_dados_pagos = []
tabelas = input("As duas tabelas estão no mesmo banco de dados (S/N) ? ")
if tabelas == 'S':
    banco_dados = input("Qual o nome do banco de dados (ex: dados.sqlite3)? ")
    tabela_refencia = input("Qual o nome da tabela que contem os valores de referencia? ")
    tabela_pagos = input("Qual o nome da tabela que contem os valores pagos? ")
    conn = sqlite3.connect(banco_dados) 
    c = conn.cursor()
elif tabelas == 'N':
    banco_dados_referencia = input("Qual o nome do banco de dados que tem os valores de referencia (ex: dados.sqlite3)? ")
    banco_dados_pagos = input("Qual o nome do banco de dados que tem os valores pagos (ex: dados2.sqlite3)? ")
    tabela_refencia = input("Qual o nome da tabela que contem os valores de referencia? ")
    tabela_pagos = input("Qual o nome da tabela que contem os valores pagos? ")
    conn = sqlite3.connect(banco_dados_referencia) 
    c = conn.cursor()
    conn = sqlite3.connect(banco_dados_pagos) 
    d = conn.cursor()
else: 
    print("Valor errado")

# SE O ID FOR O MESMO NAS DUAS TABELAS PODEMOS VERIFICAR SE O VALOR DIFERE NAS DUAS TABELAS ATRAVES DISSO

# c.execute(f'''
#           SELECT
#           *
#           FROM {tabela_refencia}
#           ''')

# valores_base = c.fetchall()
# if banco_dados_pagos:
#     c = d

# c.execute(f'''
#           SELECT
#           *
#           FROM {tabela_pagos}
#           ''')

# valores_pagos = c.fetchall()

# valor_total_base = 0
# valor_total_pago = 0
# print("Colaboradores com salarios errado:")
# print("Colaborador             Diferença")
# for row in valores_base:
#         valor_total_base += row[2]
#         valor_total_pago += valores_pagos[row[0] - 1][2]
#         if row[2] != valores_pagos[row[0] - 1][2]:
#             diferenca = valores_pagos[row[0] - 1][2] - row[2]
#             print(f'{row[1]}                {diferenca}')

# diferenca_total = valor_total_pago - valor_total_base
# print(diferenca_total)
# print(diferenca_total / len(valores_base))

# SE O ID NÂO FOR O MESMO NAS DUAS TABELAS UTILIZAREMOS BINARY SEARCH PARA ENCONTRAR PELO O NOME E ENTÂO VERIFICAR SE O VALOR DIFERE NAS DUAS TABELAS 
pdf.line(30, 710, 550, 710)


text = pdf.beginText(40, 680)
text.setFont("Helvetica", 12)
text.textLine("Colaborador com salario errado: ")
pdf.drawText(text)
def coferencia_folha(folha_referencia, folha_paga):
    folha_referencia.execute(f'''
            SELECT
            *
            FROM {tabela_refencia}
            ''')

    valores_base = folha_referencia.fetchall()


    folha_paga.execute(f'''
            SELECT
            *
            FROM {tabela_pagos} ORDER BY nome
            ''')

    valores_pagos = folha_paga.fetchall()
    valor_total_base = 0
    valor_total_pago = 0
    print("Colaboradores com salarios errado:")
    print(f"{'Colaborador': <25}Diferença")
    for row in valores_base:
            valor_total_base += row[2]
            valor_total_pago += valores_pagos[row[0] - 1][2]

            lys = len(valores_base)
            first = 0
            last = lys-1
            index = -1
            val = row[1]

            while (first <= last) and (index == -1):
                mid = (first+last)//2
                if valores_pagos[mid][1] == val:
                    index = mid
                else:
                    if val<valores_pagos[mid][1]:
                        last = mid - 1
                    else:
                        first = mid +1
            if row[2] != valores_pagos[index][2]:
                diferenca = valores_pagos[index][2] - row[2]
                espaco = len(row[1]) - 30
                print(f'{row[1] : <25}{diferenca}')
                text.textLine(f'{row[1]: <40}{diferenca}')
                pdf.drawText(text)


    diferenca_total = valor_total_pago - valor_total_base
    print(f'Diferença entre valor total das folhas: {diferenca_total}')
    print(f'Diferença media: {diferenca_total / len(valores_base)}')

    text.textLine(f'Diferença total das folhas: {diferenca_total}')
    pdf.drawText(text)
    media = diferenca_total/len(valores_base)
    text.textLine(f'Media de diferença: {media}')
    pdf.drawText(text)


    pdf.save()


if banco_dados_pagos:
    coferencia_folha(c, d)
else:
    coferencia_folha(c, c)

    