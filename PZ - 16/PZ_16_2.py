'''Создайте класс "Животное", который содержит информацию о виде и возрасте
животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
"Животное" и содержат информацию о породе.'''

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def info(self):
        print(f'Вид: {self.species}')
        print(f'Возраст: {self.age}')

class Dog(Animal):
    def __init__(self, breed, age):
        super().__init__('Собака', age)
        self.breed = breed

    def info(self):
        super().info()
        print(f'Порода: {self.breed}')

class Cat(Animal):
    def __init__(self, breed, age):
        super().__init__('Кошка', age)
        self.breed = breed

    def info(self):
        super().info()
        print(f'Порода: {self.breed}')

kitty = Cat('Шотландец-вислоухий', 4)
kitty.info()

print()

doggy = Dog('Немецкая-овчарка', 10)
doggy.info()