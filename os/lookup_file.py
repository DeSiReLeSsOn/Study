import os

"""Поиск файла в файловой системе"""




def find_file(file_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Укажите имя файла, который вы ищете, и путь к директории, в которой хотите выполнить поиск
file_name = "api.txt"
search_path = r"C:\\Users\\Admin\\Desktop"  # пример пути к директории

result = find_file(file_name, search_path)

if result:
    with open(result, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(f"Содержимое файла {file_name}:")
        print(file_content)
else:
    print(f"Файл {file_name} не найден в директории {search_path}")