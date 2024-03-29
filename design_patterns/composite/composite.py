"""Composite Design Pattern — это структурный шаблон проектирования, 
который позволяет объединять объекты в древовидные структуры для представления иерархий часть-целое. 
Это позволяет клиентам единообразно обрабатывать отдельные объекты и композиции объектов. 
В этом шаблоне один объект (лист) или группа объектов (композит) обрабатываются одинаково. 
Составной шаблон полезен, 
когда вам нужно представить иерархическую структуру объектов и вы хотите единообразно обрабатывать как отдельные объекты,
так и группы объектов. 
Это также помогает упростить код за счет уменьшения количества условных операторов, необходимых для управления объектами.

Одним из примеров шаблона составного проектирования в реальной жизни является файловая система. 
Файловая система представляет собой иерархическую структуру, состоящую из каталогов, подкаталогов и файлов. 
Каталоги могут содержать подкаталоги и файлы, а подкаталоги могут содержать дополнительные подкаталоги и файлы. 
Каждый файл и каталог можно рассматривать как отдельный объект, а каталог можно рассматривать как составной объект, 
содержащий другие объекты. 
Это позволяет пользователям выполнять операции с отдельными файлами или каталогами или с целыми каталогами и их содержимым. 
Например, пользователь может удалить один файл или весь каталог или скопировать один файл или весь каталог и его содержимое. 
Составной шаблон проектирования упрощает код для управления файловой системой, обрабатывая отдельные файлы и каталоги одинаково, 
независимо от их положения в иерархии."""


import abc


class Component(metaclass=abc.ABCMeta):
    """
    Абстракция для определения единого общего метода
    """
    @abc.abstractmethod
    def operation(self):
        pass


class Composite(Component):
    """
    Компоновщик
    """

    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class Leaf(Component):
    """
    Пример компонента
    """

    def operation(self):
        pass


def main():
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)
    composite.operation()


if __name__ == "__main__":
    main()


"""Этот код определяет три класса: Component, Composite и Leaf. 
Компонент — это абстрактный класс, определяющий метод работы, который должен быть реализован его подклассами. 
Composite является подклассом Component и представляет составной объект, который может содержать другие компоненты. 
У него есть метод init, который инициализирует пустой набор для хранения его дочерних компонентов, метод операции, 
который вызывает метод операции каждого дочернего компонента, метод добавления, 
который добавляет дочерний компонент к его набору дочерних элементов, и метод удаления, 
который удаляет дочерний компонент из его набора дочерних элементов. 
Leaf является еще одним подклассом Component и представляет собой конечный объект, не имеющий дочерних элементов. 
У него есть метод работы, который ничего не делает.

Основная функция создает экземпляр Leaf и экземпляр Composite, 
добавляет экземпляр Leaf к экземпляру Composite с помощью метода add и 
вызывает метод операции экземпляра Composite с помощью метода операции. 
Это вызовет метод операции экземпляра Leaf, даже если он содержится в экземпляре Composite.

Таким образом, будут поочередно будут запущены все методы operation() всех компонентов из набора."""