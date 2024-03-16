import abc



"""В абстрактной фабрике всегда есть продукты (то, что нам нужно получить) и фабрики 
(то, что будет создавать продукты).
Абстрактный класс содержит набор атрибутов и методов, 
которые являются необходимыми для работы этой фабрики или продукта"""




class AbstractReportBuilder(metaclass=abc.ABCMeta):
    """
    Создаем абстрактный создатель отчетов
    с необходимыми функциями
    """
    @abc.abstractmethod
    def data_collect(self):
        pass

    @abc.abstractmethod
    def create_chart(self):
        pass

    @abc.abstractmethod
    def create_diagram(self):
        pass




class WebSiteReportBuilder(AbstractReportBuilder):
    """
    Создаем конкретный создатель отчетов для сайта
    и включаем все обязательные методы родительского класса,
    которые уже будут возвращать нужные нам экземляры классов отчетов
    """
    def data_collect(self):
        pass

    def create_chart(self):
        return Chart()

    def create_diagram(self):
        return Diagram()
    



class AbstractReport(metaclass=abc.ABCMeta):
    """
    Создаем абстрактный отчет, он пока ничего не делает и не содержит
    он просто есть, но сюда можно (а в реальности нужно) включить минимальный
    и необходимый функционал и атрибутику отчетов
    """
    pass

class Chart(AbstractReport):
    """
    Конкретный отчет типа: График
    """
    pass

class Diagram(AbstractReport):
    """
    Конкретный отчет типа: Диаграмма
    """
    pass



factory = WebSiteReportBuilder()
chart = factory.create_chart()