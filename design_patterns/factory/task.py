"""Реализуйте простую игру, используя шаблон проектирования Factory Method. В игре должно быть два типа персонажей - герои и враги. У каждого персонажа должно быть имя, очки здоровья и очки атаки.
В игре должен быть абстрактный класс `Character` с тремя атрибутами – `name`, `health_points` и `attack_points`. Класс также должен иметь абстрактный метод «атака», который принимает объект другого персонажа и уменьшает его очки здоровья на очки атаки текущего персонажа.
Реализуйте два конкретных класса — «Hero» и «Enemy», которые наследуются от класса «Character». Класс Hero должен иметь дополнительный атрибут hero_type.
Реализуйте класс `CharacterFactory` с методом `create_character`, который принимает тип персонажа ("герой" или "враг") и создает экземпляр соответствующего класса. Метод create_character также должен принимать имя, очки здоровья и очки атаки персонажа.
В основном блоке создайте объект `CharacterFactory` и используйте его для создания героя и врага. Затем заставьте их атаковать друг друга по кругу, пока у одного из них не останется нулевых или отрицательных очков здоровья.
Выведите победителя игры и оставшиеся очки здоровья победителя."""


from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name, health_points, attack_points):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points

    @abstractmethod
    def attack(self, other):
        pass

class Hero(Character):
    def __init__(self, name, health_points, attack_points, hero_type):
        super().__init__(name, health_points, attack_points)
        self.hero_type = hero_type

    def attack(self, other):
        other.health_points -= self.attack_points
        return print(f"{self.name} attacks {other.name} with {self.attack_points} points.")

class Enemy(Character):
    def attack(self, other):
        other.health_points -= self.attack_points
        return print(f"{self.name} attacks {other.name} with {self.attack_points} points.")

class CharacterFactory:
    def create_character(self, character_type, name, health_points, attack_points, hero_type=None):
        self.character_type = character_type
        if self.character_type == 'enemy':
            return Enemy(name, health_points, attack_points)
        else:
            return Hero(name, health_points, attack_points, hero_type)

# Код ниже не трогаем! Нужен для проверки!
if __name__ == '__main__':
    factory = CharacterFactory()
    hero = factory.create_character('hero', 'John', 100, 20, 'Warrior')
    enemy = factory.create_character('enemy', 'Goblin', 50, 10)

    while hero.health_points > 0 and enemy.health_points > 0:
        hero.attack(enemy)
        enemy.attack(hero)

    if hero.health_points > 0:
        print(f'{hero.name} wins with {hero.health_points} health points remaining!')
    else:
        print(f'{enemy.name} wins with {enemy.health_points} health points remaining!')