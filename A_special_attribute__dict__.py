class Myclass():
    class_var = 1
    def __init__(self, i_var):
        self.i_var = i_var 

    def ASpecialAttribute(self):
        return self.__dict__

