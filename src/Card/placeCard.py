class PlaceCard:
    def __init__(self, value, pearl, ptsSKey, ptsGKey, ptsPlace, ptsPearl, sameKey, maximum, oneCoalition, draw, family):
        self.value = value
        self.pearl = pearl
        self.ptsSKey = ptsSKey
        self.ptsGKey = ptsGKey
        self.ptsPlace = ptsPlace
        self.ptsPearl = ptsPearl
        self.sameKey = sameKey
        self.maximum = maximum
        self.oneCoalition = oneCoalition
        self.draw = draw
        self.family = family

        # Getters
        def getValue(self):
            return self.value
        def getPearl(self):
            return self.pearl
        def getPtsSKey(self):
            return self.ptsSKey
        def getPtsGKey(self):
            return self.ptsGKey
        def getPtsPlace(self):
            return self.ptsPlace
        def getPtsPearl(self):
            return self.ptsPearl
        def getSameKey(self):
            return self.sameKey
        def getMaximum(self):
            return self.maximum
        def getOneCoalition(self):
            return self.oneCoalition
        def getDraw(self):
            return self.draw
        def getFamily(self):
            return self.family