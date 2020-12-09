
import sqlite3

conn = sqlite3.connect('imc.db')
cursor = conn.cursor()

p_peso = input('Peso: ')
p_altura = input('Altura: ')

tot = (float(p_peso)) / ((float(p_altura)/100) * (float(p_altura)/100))

cursor.execute("""
INSERT INTO imc (peso, altura, imc)
VALUES (?,?,?)
""", (p_peso, p_altura, tot))

conn.commit()


conn.close()