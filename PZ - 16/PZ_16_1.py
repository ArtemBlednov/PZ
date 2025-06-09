'''Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
Пол: пол.'''

class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f'Человек: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Пол: {self.gender}')
        print()


worker_human = Human('Михаил', '23', 'Мужчина')

worker_human.speak()

biker = Human('Филипп', '45', 'Мужчина')

biker.speak()