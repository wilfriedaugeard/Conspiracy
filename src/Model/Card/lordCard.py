class LordCard:
    def __init__(self, value, family, power):
        self.value = value
        self.family = family
        self.power = power


    def display(self):
        print("Lord card:",self.value, self.family.name, "| pearl:",self.power.getPearl(),"key:",self.power.getKey().name)

    #Getter
    def getValue(self):
        return self.value
    
    def getFamily(self):
        return self.family

    def getPower(self):
        return self.power

    