import random
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Communication:

    def __init__(self):

        self.Testing = input("Testing or no?")

    def getData(self):
        if (self.Testing == 'no'):

            HOST = socket.gethostname()
            PORT = 1023
            try:
                s.bind((HOST, PORT))
            except Exception:
                print("Exception Error: Unable to Open Specified Port: " + str(PORT))
                return
            s.listen()
            conn=s.accept()
            value = conn.recv(1024) # read line (single value) from the serial port
            decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
            # print(decoded_bytes)
            value_chain = decoded_bytes.split(",")
        else:
            value_chain = [0] + random.sample(range(0, 300), 1) + \
                          [random.getrandbits(1)] + random.sample(range(0, 20), 8)
        return value_chain
