from communication import Communication
from data_generator import DataGenerator
#from database import Database

communicator=Communication()
dataGen = DataGenerator()

"""
host=""
user=""
password=""
csvPath=""
base=Database(host,user,password,csvPath)
database=""
table=""
base.insertData(database,table)
"""
received_data = communicator.receivePushPull()
print(received_data)
dataGen.packed_data=received_data
dataGen.unpack()
print(dataGen.raw_data)

