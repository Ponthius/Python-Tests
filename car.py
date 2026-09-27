class car:
    
    engine_type = "Hybrid"
    Is_moving = True
    clean_status = True
    
    def cleanStatus(self):
        if self.clean_status:
            print("The car is dirty, it needs a wash.")
        else:
            print("The car is clean, it doesn't need a wash.")
    
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        
    def description(self):
        print(f"The model of the car is {self.model}.")
        print(f"The color of the car is {self.color}.")
        print(f"The year of the car is {self.year}.")
        print(f"The engine of the car is {car.engine_type}.")
        
    def moving(self):
        if self.Is_moving:
            print("The car is moving.")
        else:
            print("The car is not moving.")