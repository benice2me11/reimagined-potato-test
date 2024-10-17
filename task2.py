import sqlite3

conn = sqlite3.connect('/app/client.sqlite')
cursor = conn.cursor()

query = """
   SELECT e.name, COUNT(r.id) AS downtime_reasons_count
    FROM endpoint_reasons r
    JOIN endpoints e ON r.endpoint_id = e.id
    WHERE e.active = 'false'
    GROUP BY e.name;
"""

cursor.execute(query)

results = cursor.fetchall()
print("Количество причин простоев для каждой неактивной точки:")
for row in results:
    print(row)
    
conn.close()

