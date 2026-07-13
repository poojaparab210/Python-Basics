# Write a program that merges two dictionaries into one.

def merge_dicts(dict1,dict2):
    return {**dict1 , **dict2}

dict1 = {"a":1,"b":4}
dict2 = {"c":7,"d":9}
merge = merge_dicts(dict1,dict2)
print(merge)

#               OR

dict1 = {"a":1,"b":4}
dict2 = {"c":7,"d":9}
dict1.update(dict2)
print(dict1)
