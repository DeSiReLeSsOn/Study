import os 

print('Текущаяя директория: ', os.getcwd()) # вывести текущую директорию 

if not os.path.isdir('name_folder'):
    os.mkdir('name_folder') # создать папку в текущей директории,аргументом принимает имя


os.chdir('name_folder') # перейти в папку 'name_folder' 


os.makedirs('One/Two/Three') # создать папку One с подпапкой Two с подпапкой Three

os.rename('file_name.txt', 'new_file_name.txt') # изменить имя файла с file_name.txt на new_file_name.txt

os.replace('new_file_name.txt', 'name_folder/new_file_name.txt') # перенести папку из текущей директории в name_folder 

print(os.listdir()) # вывести название все файлов и папок в текущей директории возвращает список

for dirpach, dirnames,filenames in os.walk('.'):
    for dirname in dirnames:
        print('Каталог: ', os.path.join(dirpach, dirname))
    for filename in filenames:
        print('Файл: ', os.path.join(dirpach, filename)) # вывести все папки со всеми подфайлами в текущей директории  


    
os.remove('name_folder/new_file_name.txt') # удалить файл 

os.rmdir('folder') # удалить папку 

absolute_path = os.path.abspath('file.txt') # получение абсолютного пути 


path_variable = os.environ.get('PATH') # Получить значение переменной окружения PATH


os.startfile('os.py') # открывает файл os.py в программе установленной по умолчанию (аналог двойного клика мышкой)



