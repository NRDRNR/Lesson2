def ask_user():
    dialog = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}

    user_say = input('Введите вопрос ')
    
    if user_say in dialog.keys():
        print(dialog.get(user_say))
    else:
        print('Не знаю')


if __name__ == "__main__":
    for _ in range(10):
        ask_user()
    

