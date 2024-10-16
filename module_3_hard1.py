def calculate_structure_sum(data_structure):
    s = 0
    for i in data_structure:
        if isinstance(i,str):
            s = s + len(i)
        if isinstance(i,int):
            s+=i
        elif isinstance(i,dict):
            keys_= i.keys()
            values_ = i.values()
            s = s + calculate_structure_sum(keys_)
            s = s + calculate_structure_sum(values_)
        elif isinstance(i,tuple):
            s = s + calculate_structure_sum(i)
        elif isinstance(i,list):
            s = s + calculate_structure_sum(i)
        elif isinstance(i,set):
            s = s + calculate_structure_sum(i)
    return s
data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)