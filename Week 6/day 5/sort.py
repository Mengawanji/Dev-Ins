import psycopg2   # importing a module to connect to postgres
import psycopg2.extras

# defining our connection criteria
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'hollywoo'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

# accessing the query editor
# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# defining the query
query = "SELECT * FROM actors"

# running the query
cursor.execute(query)

# fetching the results
results = cursor.fetchall()

# closing the connection
connection.close()

# display results
for item in results:
    print(item)

