#Yılmaz Ebrar
import mysql.connector
import pandas as pd
class Database():  
    def establishConnection(self,hostname,username,passw):
        self.mydb = mysql.connector.connect(
            host = hostname,
            user = username,
            password = passw
            )
        self.cursor = self.mydb.cursor()
    
    
    def insertData(self,database,table,data):
        self.cursor.execute("USE {}".format(database))
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT, coordinates INT, time INT)".format(table))
        sqlquery = "INSERT INTO {} (id, coordinates, time) VALUES (%s, %s, %s)".format(table)
        self.cursor.executemany(sqlquery, data)
        self.mydb.commit()
    
    