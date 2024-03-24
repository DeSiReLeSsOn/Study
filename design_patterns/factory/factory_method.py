"""Фабричный метод - это паттерн проектирования, который позволяет создавать объекты без явного указания конкретного класса. 
Вместо этого, класс, который реализует фабричный метод, определяет, какой класс создать."""


"""В этом примере у нас есть абстрактный класс «Payment» с абстрактным методом «pay». 
У нас также есть два конкретных платежных класса, `CreditCardPayment` и `PaypalPayment`, которые реализуют метод `pay`.
Затем у нас есть класс `PaymentFactory` с методом `create_payment`, 
который принимает способ оплаты ("кредитная карта" или "paypal") и возвращает экземпляр соответствующего класса оплаты.
В основном блоке мы создаем экземпляр `PaymentFactory` и используем его для создания `CreditCardPayment` и `PaypalPayment`, 
которые мы затем используем для осуществления платежей. 
Мы также пытаемся создать платеж с использованием недопустимого метода оплаты, что приводит к ошибке ValueError.
В этом примере показано, как можно использовать шаблон проектирования фабричных методов для создания объектов без указания точного класса объекта, 
который будет создан. 
Делегируя ответственность за создание объекта фабричному классу, мы можем отделить клиентский код от деталей реализации конкретных классов."""

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Making a credit card payment of {amount} dollars.")
class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"Making a PayPal payment of {amount} dollars.")
class PaymentFactory:
    def create_payment(self, method):
        if method == "creditcard":
            return CreditCardPayment()
        elif method == "paypal":
            return PaypalPayment()
        else:
            raise ValueError(f"Invalid payment method {method}.")
if __name__ == "__main__":
    factory = PaymentFactory()
    payment = factory.create_payment("creditcard")
    payment.pay(100)
    payment = factory.create_payment("paypal")
    payment.pay(50)