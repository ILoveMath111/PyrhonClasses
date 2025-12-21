class BMW:
    def info(self):
        print("BMW is a German luxury car.")

class Ferrari:
    def info(self):
        print("Ferrari is an Italian sports car.")

car1 = BMW()
car2 = Ferrari()

for car in [car1, car2]:
    car.info()