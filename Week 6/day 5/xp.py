from sqlite3 import connect
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Pithagore11'
DATABASE = 'MenuItem'


class MenuItem():


    def run_query(self,query):
        connection = psycopg2.connect( host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE )
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def __init__(self,price,name):
        self.price = price
        self.name = name


    def save(self):

       # try:
            query = f"INSERT INTO restaurant(name, price) VALUES ('{self.name}',{self.price})"
            self.run_query(query)
        #except:
        #    return False

    # def delete (self):
        # query


item = MenuItem( 2000, 'Eru' )
item.save()
