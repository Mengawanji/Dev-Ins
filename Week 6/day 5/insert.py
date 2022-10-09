import psycopg2
import psycopg2.extras

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Pithagore'
DATABASE = 'dvdrental'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "SELECT * FROM customer LIMIT 20;"
cursor.execute(query)
results = cursor.fetchall()
connection.close()
for item in results:
        print(item)


