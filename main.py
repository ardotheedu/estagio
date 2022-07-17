import sqlite3

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
                     
conn.commit()