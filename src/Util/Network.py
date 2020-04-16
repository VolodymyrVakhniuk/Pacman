import socket
import threading

from queue import Queue


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

            self.__message_queue = Queue()

            self.connectionEvent = threading.Event()

            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.connectTread = threading.Thread(target=self.__connect, args=('127.0.0.1', 4040), daemon=True)
            self.connectTread.start()

            self.recieveTread = threading.Thread(target=self.recieveData, args=(), daemon=True)
            self.recieveTread.start()


        def isConnected(self):
            return self.connectionEvent.is_set()
        

        def getMessageQueue(self) -> Queue:
            return self.__message_queue


        def __connect(self, ip : str, port : int):
            self.client.connect((ip, port))
            self.connectionEvent.set()


        def recieveData(self):
            self.connectionEvent.wait()
            while True:
                data = self.client.recv(4040)
                self.__message_queue.put(data.decode("utf-8"))


        def sendData(self, data : str):
            self.client.sendall(str.encode(data))