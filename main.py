import sqlite3
import pandas as pd

conn = sqlite3.connect('dados.sqlite3') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS valores_pagos
          ([id] INTEGER PRIMARY KEY, [nome] TEXT, [salario] INTEGER)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS valores_base
          ([id] INTEGER PRIMARY KEY, [nome] TEXT, [salario] INTEGER)
          ''')

#INSERÇÂO DE DADOS PARA TESTE
        
# c.execute(''' INSERT INTO valores_base(id, nome, salario)
#         VALUES
#             (1,'Tássio Freire', 1200.35),
#             (2,'Marina de Paula', 1250.48),
#             (3,'Eduardo', 850.48)
#           '''      )

# c.execute(''' INSERT INTO valores_pagos(id, nome, salario)
#         VALUES
#             (1,'Tássio Freire', 1200.35),
#             (2,'Marina de Paula', 1300.48),
#             (3,'Eduardo', 900.48)
#           '''  )


# conn.commit()


# SE O ID FOR O MESMO NAS DUAS TABELAS PODEMOS VERIFICAR SE O VALOR DIFERE NAS DUAS TABELAS ATRAVES DISSO

# c.execute('''
#           SELECT
#           *
#           FROM valores_base
#           ''')

# valores_base = c.fetchall()

# c.execute('''
#           SELECT
#           *
#           FROM valores_pagos
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

c.execute('''
          SELECT
          *
          FROM valores_base
          ''')

valores_base = c.fetchall()
c.execute('''
          SELECT
          *
          FROM valores_pagos ORDER BY nome
          ''')

valores_pagos = c.fetchall()
valor_total_base = 0
valor_total_pago = 0
print("Colaboradores com salarios errado:")
print("Colaborador             Diferença")
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
            print(f'{row[1]}                {diferenca}')


diferenca_total = valor_total_pago - valor_total_base
print(diferenca_total)
print(diferenca_total / len(valores_base))



