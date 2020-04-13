import socket
import threading

#from Util.NetworkDataParser import NetworkDataParser



class Network(object):

    def __new__(cls):
        if not Network.__instance:
            Network.__instance = Network.__Network()

        return Network.__instance


    def __getattr__(self, name):
        return getattr(self.__instance, name)


    __instance = None


    class __Network:
        def __init__(self):
        
            self.__makeClientSocket('10.0.0.204', 4040)

            # self.recieveTread = threading.Thread(target=self.recieveData, args=(1,), daemon=True)
            # self.recieveTread.start()


        # def setRecievedDataParser(self, parser : NetworkDataParser):
        #     self.parser = parser


        def __makeClientSocket(self, ip : str, port : int):
            print("Making a socket")
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, port))


        def recieveData(self):
            #while True:
                # data = self.client.recv(4040)
                # self.recievedSrting = data.decode("utf-8")

                #self.parser.parse(self.recievedSrting)

                data = self.client.recv(4040)
                return data.decode("utf-8")


        def sendData(self, data : str):
            
            print("SENDING " + data)
            self.client.sendall(str.encode(data))


    