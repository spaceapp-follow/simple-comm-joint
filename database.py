#Yılmaz Ebrar
import mysql.connector
import pandas as pd
class Database():
    def _init_(self,host,user,password,csvPath):
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
    def insertData():
        pass
    
    