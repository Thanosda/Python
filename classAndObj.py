class Phone:
    def __init__(self):
        self.processor =""
        self.ram=""
        self.battery=""
    def reqirements(self):
       print( self.processor)
       print(self.ram)  
       print(self.battery)  

ph=Phone()
ph.processor ="i5"
ph.ram=8
ph.battery=12000       
ph.reqirements() 