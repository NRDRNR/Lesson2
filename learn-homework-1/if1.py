"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('Введите Ваш возраст: '))

def main(age):
    if 0 < age < 90:
        
        if age >= 65:
            return('Не, ну надеюсь они с пенсией больше ничего не придумают...')
        elif age >= 23:
            return('В офис завтра')
        elif age >= 17:
            return('Первую пару не проспи')
        elif age >= 6:
            return('Иди спать, завтра в школу')
        elif age >= 2:
            return('Детсад')
        elif age < 2:
            return('Мелкота')

    else: 
        print('Вы мне возраст введите, а не число от балды')
        return ('Не введён возраст')



age_test = main(age)


if __name__ == "__main__":
    print(age_test)
