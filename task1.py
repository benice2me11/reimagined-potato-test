import sqlite3

conn = sqlite3.connect('/app/client.sqlite')
cursor = conn.cursor()

query = """
    SELECT r.reason_name, r.reason_hierarchy, e.name
    FROM endpoint_reasons r
    JOIN endpoints e ON r.endpoint_id = e.id
    WHERE e.active = 'true';
"""
cursor.execute(query)

results = cursor.fetchall()
print("Причины простоя только активных станков:")
for row in results:
    print(row)

conn.close()

