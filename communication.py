import time
import zmq
import data_generator as dg

class Communication():
    def __init__(self):
        # at the beginning, we generate and pack the data
        data_object=dg.DataGenerator()
        data_object.generateData()
        data_object.packData()
        self.all_data = data_object.packed_data
    def setVariablesPubSub():
        pass
    def transmitPubSub():
        pass
    def receivePubSub():
        pass
    def setVariablesPushPull():
        pass
    def transmitPushPull(self):
        context = zmq.Context()

        sender = context.socket(zmq.PUSH)
        sender.bind("tcp://*:5556")

        for i in range(len()):
            sender.send_json(self.packed_data[i])
            print(self.packed_data[i])
            time.sleep(0.2) #200ms delay between each loop
        
        if i == len(self.packed_data) - 1:
            print("all the data is send")

    def receivePushPull(self):
        context = zmq.Context()

        receiver = context.socket(zmq.PULL)
        receiver.connect("tcp://localhost:5556")

        control_data = [] #this will help us to verify the result

        while True:
            received_data = receiver.recv_json()
            print(received_data)
            control_data.append(received_data)

            if len(control_data) == len(self.packed_data):
                break

        print("all the data is received")
