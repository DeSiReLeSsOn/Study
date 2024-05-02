import hashlib
import os

password = "123456789s".encode('utf-8')
hashed_password = hashlib.sha256(password).hexdigest()

print(hashed_password) # выводим хеш пароля 

"""Соль и хеширование паролей
Для увеличения безопасности, в добавок к хешированию паролей, можно использовать "соль". 
Соль – это уникальные данные, которые добавляются к паролю перед хешированием."""



password = "my_password"
salt = os.urandom(16)

hashed_password2 = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000) # хешируем пароль по алгоритму sha256

print(hashed_password2)



"""Библиотека Passlib
Еще одним вариантом является использование библиотеки Passlib. 
Эта библиотека предоставляет большие возможности для работы с паролями и обеспечивает высокий уровень безопасности.

Пример использования Passlib"""

from passlib.hash import pbkdf2_sha256


password = "your_password"
hashed_password3 = pbkdf2_sha256.hash(password)

print(hashed_password3)

if pbkdf2_sha256.verify(password, hashed_password3):
    print("Пароли совпадают")
else:
    print("Пароли не совпадают")