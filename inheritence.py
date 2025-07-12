class Vehicle:   # parent
    def move(self):
        print("Moving...")

class Car(Vehicle): # child
    def honk(self):
        print("Beep beep!")
    pass
my_car = Car()  # i am calling here child class then i getting parent class output here

my_car.move()  # Inherited method
