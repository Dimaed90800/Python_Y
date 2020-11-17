class Summator:
    def transform(self,n):
        return n
    
    def sum(self,N):
        a=0
        for i in range(1, N+1):
            a+=self.transform(i)
        return a

class PowerSummator(Summator):
    def __init__(self, b):
        self.b=b
        
    def transform(self,n):
            return n    
        
    def sum(self,N):
        a=0
        for i in range(1, N+1):
            a+=self.transform(i)**self.b
        return a

class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)
        
        
class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
   
    
