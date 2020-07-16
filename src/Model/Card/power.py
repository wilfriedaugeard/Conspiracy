class Power:
    def __init__(self, key, pearl, switch, draw):
        self.key = key
        self.pearl = pearl
        self.switch = switch
        self.draw = draw


    
    # Getters
    def getPearl(self):
        return self.pearl

    def getKey(self):
        return self.key
        
    def getSwitch(self):
        return self.switch

    def getDraw(self):
        return self.draw
