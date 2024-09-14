class hashSet:
    def __init__(self) -> None:
        self.sett = set() 
        
    def add(self,val):
        self.sett.add(val)   
         
    def remove(self,val):
        if val in self.sett:
            self.sett.remove(val) 
            
    def contains(self,val):
        return val in self.sett           