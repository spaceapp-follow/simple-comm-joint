#Yılmaz Ebrar

class Database():
    def __init__(self):
        pass
    def insertData():
        self.cursor.execute("USE {}".format(database))
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT, coordinates INT, time INT)".format(table))
        sqlquery = "INSERT INTO {} (id, coordinates, time) VALUES (%s, %s, %s)".format(table)
        self.cursor.executemany(sqlquery, self.data)
        self.mydb.commit()
    
    