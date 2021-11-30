def count_names(lst_of_dicts):
    counted_names_dict = {}
    for i in lst_of_dicts:
        name = i['first_name']
        if name in counted_names_dict:
            counted_names_dict[name] += 1
        else:
            counted_names_dict[name] = 1

    return counted_names_dict


def find_most_frequent_name(counted_names_dict):
    most_frequent_name = sorted(counted_names_dict.items(), key=lambda x: x[1], reverse=True)[0]
    return most_frequent_name


def count_girls_and_boys(lst_of_dicts, is_male):
    girls = 0
    boys = 0
    for student in lst_of_dicts['students']:
        name = student.get('first_name')
        if is_male[name]:
            boys += 1
        else:
            girls += 1
    
    return girls, boys


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('\nЗадание 1')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

counted_names = count_names(students)
for name in counted_names:
    print(f'{name}: {counted_names[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print('\nЗадание 2')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

counted_names = count_names(students)
the_most_frequent_name = find_most_frequent_name(counted_names)
print(f'Самое частое имя среди учеников: {the_most_frequent_name[0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print('\nЗадание 3')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for cls in school_students:
    counted_names = count_names(cls)
    the_most_frequent_name = find_most_frequent_name(counted_names)
    print(f'Самое частое имя в классе {school_students.index(cls) + 1}: {the_most_frequent_name[0]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
print('\nЗадание 4')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for cls in school:
    genders = count_girls_and_boys(cls, is_male)
    print(f'Класс {cls["class"]}: девочки {genders[0]}, мальчики {genders[1]}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print('\nЗадание 5')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    #{'class': '4c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}, {'first_name': 'Олег'},]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

max_girls_class = ['', 0]
max_boys_class = ['', 0]

for cls in school:
    genders = count_girls_and_boys(cls, is_male)

    if genders[0] > max_girls_class[1]:
        max_girls_class = [cls['class'], genders[0]]

    if genders[1] > max_boys_class[1]:
        max_boys_class = [cls['class'], genders[1]]

print(f'Больше всего девочек в классе {max_girls_class[0]}')
print(f'Больше всего мальчиков в классе {max_boys_class[0]}') 
