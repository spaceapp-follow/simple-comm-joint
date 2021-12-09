import time
import zmq
import data_generator as dg

class Communication():
    def __init__(self,flag=0):
        # at the beginning, we generate and pack the data
        data_object=dg.DataGenerator()
        if flag==1:
            data_object.generateFloatData()
            data_object.packFloatData()
            self.all_data=data_object.packed_data
        else:
            print("here")
            data_object.generateData()
            data_object.packData()
            self.all_data = data_object.packed_data
        self.address = "tcp://*:5555"

    def transmitPubSub(self):
        pubctx = zmq.Context()
        self.sender = pubctx.socket(zmq.PUB)
        self.sender.bind(self.address)

        for packet_index in range(len(self.all_data)):
            self.message = self.all_data[packet_index]
            self.sender.send_pyobj(self.message)
    
    def receivePubSub(self,pack_len):
        subctx = zmq.Context()
        receiver = subctx.socket(zmq.SUB)

        receiver.connect(self.address)
        receiver.setsockopt_string(zmq.SUBSCRIBE, '')
        self.all_data = []
        message=""
        while message!='0'*pack_len:
            message = receiver.recv_pyobj()
            print(message)
            self.all_data.append(message)
            
    def transmitPushPull(self):
        context = zmq.Context()
        sender = context.socket(zmq.PUSH)
        sender.bind("tcp://*:5556")
        for i in range(len(self.all_data)):
            sender.send_json(self.all_data[i])
            print(self.all_data[i])
            time.sleep(0.2) #200ms delay between each loop
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

            if len(control_data) == len(self.all_data):
                break

        print("all the data is received")
        return control_data
