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



