class Fruit:
    def __init__(self,name , color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def isfresh(self):
        if self.color == "brown":
            return False
        else:
            return True

    def __str__(self):
        return("Name: "+str(self.name) + "\nColor: "+str(self.color) + "\nWeight: " + str(self.weight)+ "\nIt is fresh: "+str(self.isfresh())+"\n")

class Banana(Fruit):
    def __init__(self):
        super().__init__("Banana", "Yellow", "200g")

class Apple(Fruit):
    def __init__(self):
        super().__init__("Apple", "Red", "150g")

banana=Banana()
print(banana)