#AHMET ve ENES
import zmq

class Communication():
    def __init__(self):
        self.address = "tcp://*:5555"


        pass

    
    def setVariablesPubSub(self):

        pass
    def transmitPubSub(self,packed_data,length):

            pubctx = zmq.Context()
            self.sender = pubctx.socket(zmq.PUB)
            self.sender.bind(self.address)

            for self.packet_count in range(length):
                self.message = packed_data[self.packet_count]   
                self.sender.send_pyobj(self.message)


        
    def receivePubSub(self,length):
        subctx = zmq.Context()

        receiver = subctx.socket(zmq.SUB)

        receiver.connect(self.address)
        receiver.setsockopt_string(zmq.SUBSCRIBE, '')
        self.all_data = []
        while True:

            message = receiver.recv_pyobj()
    
            print(message)


            if len(self.all_data) < length :
                self.all_data.append(message)
            else:
                break
        pass
    def setVariablesPushPull():
        pass
    def transmitPushPull():
        pass
    def receivePushPull():
        pass
