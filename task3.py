import sqlite3

conn = sqlite3.connect('/app/client.sqlite')
cursor = conn.cursor()

query = """
    SELECT e.name, r.reason_hierarchy, COUNT(r.id) AS downtime_reasons_count
    FROM endpoint_reasons r
    JOIN endpoints e ON r.endpoint_id = e.id
    WHERE e.active = 'true' 
    AND r.reason_name = 'Перебои напряжения'
    GROUP BY e.name, r.reason_hierarchy;
"""

cursor.execute(query)

results = cursor.fetchall()
print("Активное оборудование с причиной протсоя Перебои напряжения:")
for row in results:
    print(row)
    
conn.close()
