"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    data_storage = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2, 3, 5]},
                    {'school_class': '4b', 'scores': [3, 2, 2, 5, 2, 5]},
                    {'school_class': '5a', 'scores': [3, 4, 5, 5, 2, 2]},
                    {'school_class': '4b', 'scores': [5, 4, 2, 5, 2]},
                    {'school_class': '6a', 'scores': [4, 4, 4, 3, 5, 2, 2]},
                    {'school_class': '6b', 'scores': [3, 3, 5, 5]}]

    classes_grade = {item['school_class']:(sum(item['scores'])/len(item['scores'])) for item in data_storage}
    school_grade = sum(classes_grade.values()) / len(classes_grade.values())
    
    print("School summary grade is " + '{:.2f}'.format(school_grade))
    print("Class summary grade are:")
    for name_class, grade_class in classes_grade.items():
        print("{}: {:.2f}".format(name_class,grade_class))

    
    
if __name__ == "__main__":
    main()
