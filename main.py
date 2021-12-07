from communication import Communication
from data_generator import DataGenerator
from database import Database

communicator=Communication()
host=""
user=""
password=""
csvPath=""
base=Database(host,user,password,csvPath)
database=""
table=""
base.insertData(database,table)