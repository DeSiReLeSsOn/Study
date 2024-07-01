""" 
    Напишите функцию `get_top_students(students)`, которая принимает список словарей, 
    представляющих студентов, и возвращает список из 3-х студентов с наивысшим средним баллом. 
    входные данные:
    students = [
    {'name': 'Иван', 'grades': [5, 4, 3, 5]},
    {'name': 'Мария', 'grades': [4, 5, 4, 4]},
    {'name': 'Петр', 'grades': [3, 4, 5, 5]},
    {'name': 'Ольга', 'grades': [5, 5, 5, 5]},
    {'name': 'Дмитрий', 'grades': [4, 4, 4, 4]},
]    
""" 


students = [
    {'name': 'Иван', 'grades': [5, 4, 3, 5]},
    {'name': 'Мария', 'grades': [4, 5, 4, 4]},
    {'name': 'Петр', 'grades': [3, 4, 5, 5]},
    {'name': 'Ольга', 'grades': [5, 5, 5, 5]},
    {'name': 'Дмитрий', 'grades': [4, 4, 4, 4]},
] 



def get_top_students(students:list):
    for i in students:
        i['average_grade'] = sum(i['grades']) / len(i['grades'])
    sorted_studens = sorted(students, key=lambda x: x['average_grade'], reverse=True)
        
    return sorted_studens[:3]
        
    
    
        
print(get_top_students(students))
        