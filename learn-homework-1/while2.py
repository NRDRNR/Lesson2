"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    dialog = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}

    user_say = input('Введите вопрос ')
    
    if user_say in dialog.keys():
        print(dialog.get(user_say))
            
    else:
        print('Не знаю')
            
                


if __name__ == "__main__":
    while True:
        ask_user()
    

