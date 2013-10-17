class person(object):
    def __init__(self):
        self.name = None
        self.height = None
        self.race = None
    def setName(self,n):
        """Allows the instances name to be set"""
        self.name = n
    def setHeight(self,h):
        """Allows the instances height to be set"""
        self.height = h
    def setRace(self,r):
        """Allows the instances race to be set"""
        self.race = r
    def getAllAttributes(self):
        """Returns a tuple containing all attribute information"""
        return self.name,self.height,self.race

        
