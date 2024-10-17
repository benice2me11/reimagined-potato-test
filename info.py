import sqlite3

conn = sqlite3.connect('client.sqlite')
cursor = conn.cursor()

def print_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Данные из таблицы {table_name}:")
    
    if rows:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [description[1] for description in cursor.fetchall()]
        print(f"Столбцы: {', '.join(columns)}")
        
        for row in rows:
            print(row)
    else:
        print("Таблица пуста.")
    print("\n")

tables = ['endpoints', 'endpoint_reasons', 'endpoint_groups']

for table in tables:
    print_table_data(table)

conn.close()

