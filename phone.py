class phone:
    def __init__(self,model,battery):
        self.model = model
        self.battery = battery
    
    def use_phone(self):
        if self.battery - 5 > 0:
            self.battery -= 5
            print(f"Phone used, battery is now {self.battery}%")
        else:
            print("Phone battery has ran out, shutting down.....")

phone1 = phone("Samsung s25",3)
phone1.use_phone()