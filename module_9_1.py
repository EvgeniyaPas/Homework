def min(args):
    minim = args[0]
    for i in args:
        if i < minim:
            minim = i
    return minim

def max(args):
    maxim = args[0]
    for i in args:
        if i > maxim:
            maxim = i
    return maxim

def len(args):
    k = 0
    for i in args:
        k += 1
    return k

def sum(args):
    summa = 0
    for i in args:
        summa += i
    return summa

def sorted(args):
    for i in range(len(args)):
        lowest = i
        for j in range(i + 1, len(args)):
            if args[j] < args[lowest]:
                lowest = j
        args[i], args[lowest] = args[lowest], args[i]
    return args




def apply_all_func(int_list, *functions):
    result = {}
    for f in functions:
        res = f(int_list)
        result[f.__name__] = res
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))