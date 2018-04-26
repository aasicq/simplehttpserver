import psycopg2
import json

class Postgres():
    def __init__(self):
        self.conn = psycopg2.connect("dbname=student user=postgres password=aashiq123")
        self.c = self.conn.cursor()

        


    def create_table(self):
        
        self.c.execute("CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY, name TEXT, age INT, address TEXT)")
        self.conn.commit()

    def insert_content(self):
        raw = json.load(open('/home/aashiq/Desktop/firstweek/postgresql/dat.json'))
        for i in raw:
            self.c.execute(f"INSERT INTO students(age, name, address) VALUES ({i['age']}, '{i['name']}', '{i['address']}')")        
            self.conn.commit()
        
    
    def read_db(self):
        self.c.execute("SELECT * FROM students")
        return self.c.fetchall()
            
    def delete_db(self, id):
        self.c.execute(f"DELETE FROM students WHERE id={id}")
        self.conn.commit()
        

    def read_id(self, id):
        dictformat = {}
        self.c.execute(f"SELECT * FROM students WHERE id={id}")
        for row in self.c.fetchall():
            dictformat['id']=row[0]
            dictformat['name']= row[1]
            dictformat['age']=row[2]
            dictformat['address']=row[3]
        
        return dictformat

        
if __name__=='__main__':
    database=Postgres()
    # database.read_id(int(input()))
    database.read_db()
    # database.delete_db(2)