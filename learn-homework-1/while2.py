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
    
    def ask_user_dict():

        user_say = input()
        while True:
            if user_say == dialog.items:
                print(1)
                ask_user_dict()
            else:
                print('Не знаю')
                ask_user_dict()


    ask_user_dict()

if __name__ == "__main__":
    ask_user()
    

