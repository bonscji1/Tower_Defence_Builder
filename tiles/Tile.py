

class Tile:
    '''Parent class for all tiles'''
    #TODO: change this to modular later
    NUM64 = 64

    def __init__(self,):
        width : int = self.NUM64 #in bits
        height: int = self.NUM64
        sprite = None


    def load_sprite(self, name):
        print(name)
