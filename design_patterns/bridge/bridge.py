"""Шаблон проектирования моста — это структурный шаблон проектирования, который отделяет абстракцию от ее реализации, 
так что они могут варьироваться независимо друг от друга. 
Он включает в себя создание двух отдельных иерархий, одну для абстракции и одну для реализации, 
а затем установление связи между ними. Таким образом, изменения в реализации не повлияют на абстракцию, 
а изменения в абстракции не повлияют на реализацию. Этот шаблон полезен, 
когда существует несколько вариантов абстракции или реализации, и когда изменения в одном не должны влиять на другие. 
Это способствует гибкости, расширяемости и ремонтопригодности."""



# Abstraction
class Weapon:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.enchantment = None
    def attack(self):
        pass
# Implementation
class Sword:
    def __init__(self):
        self.damage = 10
    def attack(self):
        print("Swinging sword for {} damage".format(self.damage))
class Axe:
    def __init__(self):
        self.damage = 15
    def attack(self):
        print("Chopping axe for {} damage".format(self.damage))
# Bridge
class EnchantedWeapon(Weapon):
    def __init__(self, weapon, enchantment):
        self.weapon = weapon
        self.enchantment = enchantment
    def attack(self):
        self.weapon.attack()
        if self.enchantment:
            print("Applying enchantment: {}".format(self.enchantment))

# Usage
sword = Weapon("Sword")
axe = Weapon("Axe")
sword_weapon = Sword()
enchanted_sword = EnchantedWeapon(sword_weapon, "Fire")
axe_weapon = Axe()
enchanted_axe = EnchantedWeapon(axe_weapon, "Ice")
enchanted_sword.attack() # Swinging sword for 10 damage, Applying enchantment: Fire
enchanted_axe.attack() # Chopping axe for 15 damage, Applying enchantment: Ice



"""В этом примере класс «Weapon» представляет собой абстракцию для различных типов оружия, 
которое можно использовать в игре. Классы `Sword` и `Axe` представляют собой разные реализации класса `Weapon`, 
каждая из которых имеет собственный метод `attack()`, выполняющий различные типы атак.
Класс EnchantedWeapon представляет собой мост между абстракцией и реализацией. 
Он принимает экземпляр реализации «Оружие» и чары в качестве параметров и использует их для выполнения атаки. 
Метод `attack()` класса `EnchantedWeapon` вызывает метод `attack()` базовой реализации `Weapon`, 
а затем применяет чары, если они предоставлены.
Этот шаблон проектирования позволяет легко расширять систему вооружения игры в будущем, 
просто создавая новые реализации класса `Weapon` и используя класс `EnchantedWeapon` для соединения абстракции и реализации."""
