from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

class Toyota(Car):
    def get_description(self):
        return "Toyota"

    def cost(self):
        return 20000

class BMW(Car):
    def get_description(self):
        return "BMW"

    def cost(self):
        return 50000

class CarDecorator(Car):
    def __init__(self, car):
        self.car = car

    def get_description(self):
        return self.car.get_description()

    def cost(self):
        return self.car.cost()

class HeatedSeats(CarDecorator):
    def get_description(self):
        return self.car.get_description() + ", Heated Seats"

    def cost(self):
        return self.car.cost() + 1000

class PanoramicRoof(CarDecorator):
    def get_description(self):
        return self.car.get_description() + ", Panoramic Roof"

    def cost(self):
        return self.car.cost() + 2000

def main():
    car = Toyota()
    print(car.get_description(), "cost:", car.cost())
    
    car = HeatedSeats(car)
    print(car.get_description(), "cost:", car.cost())

    car = BMW()
    print(car.get_description(), "cost:", car.cost())
    
    car = PanoramicRoof(car)
    print(car.get_description(), "cost:", car.cost())

if __name__ == "__main__":
    main()