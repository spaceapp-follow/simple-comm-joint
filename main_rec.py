from communication import Communication
from data_generator import DataGenerator
from database import Database

communicator=Communication(1)
dataGen = DataGenerator()

flag=1
#flag=1 means float, 0 means int
received_data = communicator.receivePushPull()
print(received_data)
dataGen.packed_data=received_data
dataGen.unpackFloat()

print(dataGen.raw_data)
print("All data is converted")

host="127.0.0.1"
user="ebrar"
password="Qdvnl.22"
csvPath=""

base=Database()
base.establishConnection(host,user,password)
database="tubitakdatabase"
table="data1"
if(flag):
    base.insertFloatData(database,table,dataGen.raw_data)
else:
    base.insertData(database,table,dataGen.raw_data)
print("All data is inserted into database")



