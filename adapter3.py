class SocketAdapter():
    """
       SocketAdapter base class 
    """
    def __init__ (self ):
        pass

    def convert(self ):
        pass

    def getSocket (self):
        pass


class AnyToChineseAdapter(SocketAdapter):
    """
       A concrete SocketAdapter class that can convert any socket to chinese socket
    """

    def __init__ (self):
        super().__init__()
        self.__outSocket = chineseSocket()
        self.__voltRatio = 1
        self.__plug = ""

    def convert(self, fromSocket):
        res = True
        if  isinstance (fromSocket,  chineseSocket):
            self.__voltRatio = 1
            self.__plug = "Chinese format Plug"
            print("Chinese to Chinese using {}".format(self.__plug))
        elif isinstance (fromSocket,  europeanSocket):
            self.__voltRatio = 1
            self.__plug = "European format Plug"
            print("European to Chinese using {}".format(self.__plug))
        elif isinstance (fromSocket,  taiwaneseSocket):
            self.__voltRatio = 2
            self.__plug = "Taiwanese format Plug"
            print("Taiwanese to Chinese using {}".format(self.__plug))
        # elif     isinstance (fromSocket,  someSocket):
        #    do converting stuff...
        else:        
            print("Unknown socket, cannot choose plug format and volt convertion ratio")
            res = False
        return res

    def getSocket(self):
        return self.__outSocket

    def getVoltRatio(self):
        return self.__voltRatio
