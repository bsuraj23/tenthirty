class employee :
    def __init__(self, name,empid):
        self.name= name
        self.empid=empid
        
    def show( self):
         print(f"employee name is {self.name} and his id is {self.empid}")
         
class manager(employee):
    def __init__(self, name, empid,teamsize):
        super().__init__(name, empid)   
        self.teamsize= teamsize
    def team(self):
         print(f"{self.name} manages team of {self.teamsize} employees")      
        
class seniormanager(manager)  :
    def __init__(self, name, empid, teamsize,fund):
        super().__init__(name, empid, teamsize)
        self.fund= fund
    def fundmoney(self):
           print(f"{self.name} manages fund of {self.fund} lakh rupees ")
        
sm=  seniormanager("soham",111,15,50)
sm.show()
sm.team()
sm.fundmoney()
    
