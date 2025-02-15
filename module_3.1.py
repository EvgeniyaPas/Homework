Домашняя работа по уроку "Пространство имён"
Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих модулей.

Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).

Пример результата выполнения программы:
Пример выполняемого кода:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
Вывод на консоль:
(8, 'CAPYBARA', 'capybara')
(10, 'ARMAGEDDON', 'armageddon')
True
False
4
Примечания:
Для использования глобальной переменной внутри функции используйте оператор global.
Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.

calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    tuple = (len(string), string.lower(), string.upper())
    print(tuple)
    count_calls()
def is_contains(string,list_to_search):
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    string = string.lower()
    print(string in list_to_search)
    count_calls()
string_info('Холодильник')
string_info('Стол')
is_contains('BANan', ['ban', 'BaNaN', 'urBAN'])
is_contains('Cyclic', ['recycling', 'cyclic'])
print(calls)



