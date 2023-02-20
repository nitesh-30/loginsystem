import mysql.connector

class DatabaseConnector:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='main')
            self.mycursor = self.conn.cursor()
        except:
            print("Error occured")
        else:
            print('successfully connected')

    def register(self, name, email, password):
        try:
            sql = "INSERT INTO info (name, email, password) VALUES (%s, %s, %s)"
            val = (name, email, password)
            self.mycursor.execute(sql, val)
            self.conn.commit()
        except:
            print('Not connected')
            return False
        else:
            print('connected')
            return True

    def search(self, email, password):
        self.mycursor.execute("""SELECT * FROM info WHERE email LIKE '{}' AND password LIKE '{}' """.format(email, password))
        return self.mycursor.fetchall()