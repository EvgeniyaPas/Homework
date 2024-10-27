def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'
    return inner_function()
# a = inner_function(x)
b = test_function()
print(b)
# print(a)