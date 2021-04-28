# https://dev.to/jemaloqiu/design-pattern-in-python-4-adapter-pattern-g74
class PowerSocket():
    """
       PowerSocket base class 
    """
    def __init__ (self, holeNum, Shape, Volt):
        self.__num_holes = holeNum
        self.__hole_shape = Shape
        self.__volt = Volt

    def getHoleNum (self):
        return self.__num_holes 

    def getHoleShape (self):
        return self.__hole_shape 

    def getVolt (self):
        return self.__volt 

### some concrete PowerSocket classes
class chineseSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 3, "FLAT", 220)  
class europeanSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 2, "ROUND", 220)          
class taiwaneseSocket(PowerSocket):
    def __init__ (self):
        super().__init__( 2, "FLAT", 110) 


class chinise3pinPlug():
    def __init__ (self):
        self.pins = 3
        self.volt = 220
        self.pinshape = "FLAT"    

class RedmiLaptop():

    def __init__ (self):
        self.plug = chinise3pinPlug()


    def charge(self, socket, powerInWatt):
        res = False     
        if (isinstance(socket, PowerSocket)):
            res = (self.plug.pins == socket.getHoleNum() )  and \
            (self.plug.pinshape == socket.getHoleShape() ) and  \
            (self.plug.volt == socket.getVolt() )
        else:
            print ("Socket is not instance of PowerSocket")

        if res:
            current = round(powerInWatt / self.plug.volt, 2)
            print("Start charging... Power: {} watt; Socket current: {} am ...".format(str(powerInWatt), str(current)))
        else:
            print("Socket and plug not compatible, impossible to charge.")
        return res

if __name__ == "__main__":

    laptop = RedmiLaptop() # instance of my Redmi Laptop

    # I am in china mainland
    chSocket = chineseSocket()
    laptop.charge(socket=chSocket, powerInWatt=235)

    # I am in France
    euSocket = europeanSocket()
    laptop.charge(socket=euSocket, powerInWatt=235)

    # I am in Taipei 
    twSocket = taiwaneseSocket()
    laptop.charge(socket=twSocket, powerInWatt=235)
