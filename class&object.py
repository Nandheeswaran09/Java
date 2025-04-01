#car 
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def pro(self):
        print(f'This is { self.year} ,{self.make}, {self.model}')
        print('This is starting')
        print('This is stopping')
        
        

c1=car('Toyota','corolla',2020)
c1.pro()
