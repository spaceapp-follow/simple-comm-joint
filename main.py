from communication import Communication
from data_generator import DataGenerator


#flag=1 sends float, no flag means send int
communicator=Communication(flag=1)
communicator.transmitPushPull()
