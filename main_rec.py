from communication import Communication
from data_generator import DataGenerator
from database import Database

communicator=Communication()
dataGen = DataGenerator()

received_data = communicator.receivePushPull()
print(received_data)
dataGen.packed_data=received_data
dataGen.unpack()

print(dataGen.raw_data)

host="127.0.0.1"
user="ebrar"
password="Qdvnl.22"
csvPath=""

base=Database()
base.establishConnection(host,user,password)
database="tubitakdatabase"
table="data1"

base.insertData(database,table,dataGen.raw_data)



