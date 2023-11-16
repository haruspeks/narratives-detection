import psycopg2
import os

class Data:

   conn = None

   def __init__(self):
      user_id = os.environ.get('User_ID')
      password = os.environ.get('Password')
      host = os.environ.get('Host')
      port = os.environ.get('Port')
      database =  os.environ.get('Database')
      
      connection_string = f'user={user_id} password={password} host={host} port={port} dbname={database}' 
      print(connection_string)
      try:
         self.conn = psycopg2.connect(connection_string)
      except Exception as ex:
         print(f'Unable to connect to the database {ex}')

   def get(self, id):
      print('get')
      with self.conn.cursor() as cursor:
         try: 
            cursor.execute("SELECT version()")
            single_row = cursor.fetchone()
            print(f"{single_row}")
        
         except (Exception, psycopg2.DatabaseError) as error:
            print(error)

      return True
