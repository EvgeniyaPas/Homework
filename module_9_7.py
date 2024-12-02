def is_prime(func):
    def prostoye_or_sostavnoye(*args):
        result = func(*args)
        k = 0
        for i in range(1, result + 1):
            if result % i == 0:
                k += 1
        if k == 2:
            print('Простое')
        if k > 2:
            print('Составное')
        return result
    return prostoye_or_sostavnoye

@ is_prime
def sum_three(*args):
    s = 0
    for number in args:
        s += number
    return s


result = sum_three(2, 4, 6)
print(result)
