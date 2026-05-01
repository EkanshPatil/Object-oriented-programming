class camera:
    def __init__(self,megapixels):
        self.megapixels = megapixels

    def shoot(self):
        return f"Capturing photos and videos with {self.megapixels} megapixel camera"
    
class phone:
    def __init__(self,storage,network,brand):
        self.storage = storage
        self.network = network
        self.brand = brand
    
    def call(self):
        return f"calling and messaging from {self.brand}"
    
class smartphone(camera,phone):
    def __init__(self, megapixels,storage,network,brand):
        camera.__init__(self,megapixels)
        phone.__init__(self,storage,network,brand)
    def properties(self):
        return "browsing the internet"

c = camera(20)
p = phone("Samsung",64,"5G")
s = smartphone(40,64,"5G","OnePlus")
print(s.shoot())
print(s.call())
