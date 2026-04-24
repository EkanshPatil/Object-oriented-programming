class car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def increase_speed(self,A):
        self.speed += A
        print(f"car is running at the speed of {self.speed}")
    
    def decrease_speed(self,D):
        if self.speed - D > 0:
            self.speed -= D
            print(f"the car is running at the speed of {self.speed}")
        else:
            print("the car has stopped")

car1 = car("Mercedes",98)
car1.increase_speed(20)
car1.decrease_speed(80)
car1.decrease_speed(40)       