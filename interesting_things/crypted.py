# установим библиотеку pyaescrypt командой : pip3 install pyaescrypt
import pyAesCrypt

password = input('Введите пароль для шифрования: ')


# шифруем файл 
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password) #первый агрумент путь к файлу который хотим зашифровать, вторым имя файла на выходе, третьим -пароль  



# дешифруем файл
pyAesCrypt.decryptFile('data.txt.aes', 'dataout,txt', password) # первуй агрумент путь к зашифрованному файлу, вторым уже готовый расшифрованный файл, третьим - пароль  