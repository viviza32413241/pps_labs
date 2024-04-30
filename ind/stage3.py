from abc import ABC, abstractmethod

class Furniture(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Table(Furniture):
    def __str__(self):
        return "Table"

class Chair(Furniture):
    def __str__(self):
        return "Chair"

class Bed(Furniture):
    def __str__(self):
        return "Bed"


class Wood(Material):
    def __str__(self):
        return "Wood"

class Metal(Material):
    def __str__(self):
        return "Metal"


class AbstractFactory(ABC):
    @abstractmethod
    def create_furniture(self):
        pass

    @abstractmethod
    def create_material(self):
        pass


class WoodenFurnitureFactory(AbstractFactory):
    def create_furniture(self):
        return Table()

    def create_material(self):
        return Wood()

class MetalFurnitureFactory(AbstractFactory):
    def create_furniture(self):
        return Chair()

    def create_material(self):
        return Metal()


def client_code(factory: AbstractFactory):
    furniture = factory.create_furniture()
    material = factory.create_material()
    print(f"Creating {furniture} with {material}")


wooden_factory = WoodenFurnitureFactory()
client_code(wooden_factory)

metal_factory = MetalFurnitureFactory()
client_code(metal_factory)