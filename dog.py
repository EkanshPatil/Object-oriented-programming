class dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
         print("Bark Bark!") 

dog1 = dog("barker","golden retriever")
dog1.bark()