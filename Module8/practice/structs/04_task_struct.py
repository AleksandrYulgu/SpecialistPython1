# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

#uni_dict = {**dictionary_2, **dictionary_2}
#print(uni_dict)
uni_dict2 = dictionary_1.copy()
uni_dict2.update(dictionary_2)
print(uni_dict2)
