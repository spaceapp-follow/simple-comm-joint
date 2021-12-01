#Yılmaz Ebrar
import pandas as pd
import mysql.connector
class Database():
    def __init__(self,host,user,password,csvPath):
        self.host = host
        self.user = user
        self.password = password
        self.mydb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password
            )
        self.cursor = self.mydb.cursor()
        csv = pd.read_csv(csvPath)
        id = csv[['id']].values.tolist()
        coordinates = csv[['coordinates']].values.tolist()
        time = csv[['time']].values.tolist()
        self.data = [id,coordinates,time]
    def insertData(self,database,table):
        
        self.cursor.execute("USE {}".format(database))
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT, coordinates INT, time INT)".format(table))
        sqlquery = "INSERT INTO {} (id, coordinates, time) VALUES (%s, %s, %s)".format(table)
        self.cursor.executemany(sqlquery, self.data)
        self.mydb.commit()
    