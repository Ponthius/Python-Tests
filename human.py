class human:
    
    gender = "male"
    #eatStatus = False
    
    def canEat(self):
        if self.eatStatus:
            print(f"{self.name} can eat food.")
        else:
            print(f"{self.name} can not eat food.")
    
    def __init__(self, name, shirt, pants, shoes, hat, is_alive, eatStatus):
        self.eatStatus = eatStatus
        self.shirt = shirt
        self.pants = pants
        self.shoes = shoes
        self.hat = hat
        self.name = name
        self.is_alive = is_alive
        
    def walk(self):
        print(f"{self.name} is walking in {self.shoes} shoes.")
        
    def torso(self):
        print(f"{self.name} is wearing an {self.shirt} shirt.")
        
    def pantsStatus(self):
        print(f"{self.name} has {self.pants} pants.")
        
    def hatStatus(self):
        print(f"{self.name} has a {self.hat}.")
        
    def aliveStatus(self):
        if self.is_alive == True:
            print(f"{self.name} is alive.")
        else:
            print(f"{self.name} is not alive.")
            
    def sex(self):
        print(f"{self.name} is {human.gender}")
        