class Frob:
    def __init__(self, bamf):
        self.bamf = bamf 

    def __getattr__(self, name):
        return 'Frob does not have {} attribute.'.format(str(name))


if __name__=='__main__':

    f = Frob('bamf')                
    f.bar 
    f.bamf


