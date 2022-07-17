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

             
c.execute(''' INSERT INTO valores_base(id, nome, salario)
        VALUES
            (1,'Tássio Freire', 1200.35),
            (2,'Marina de Paula', 1250.48),
            (3,'Eduardo', 850.48)
          '''      )

c.execute(''' INSERT INTO valores_pagos(id, nome, salario)
        VALUES
            (1,'Tássio Freire', 1200.35),
            (2,'Marina de Paula', 1300.48),
            (3,'Eduardo', 900.48)
          '''  )


conn.commit()
