"""
Изменить реализацию функции рекурсивного поиска элемента в словаре (из предыдущего задания)
следующим образом:
- функция должна находить ПЕРВОЕ соответствие имени и возвращать результат в виде словаря:

    {'val': found_value, 'parent': found_value_parent, 'deep': found_value_deep}

"""

def recursive_search(source_dict, lookup_value, deep=-1, parent=None):
    """ Your code is here """

    if len(source_dict) == 0:
        return 0

    lst = {}
    for k, v in source_dict.items():
        if isinstance(v, dict):
            deep += 1
            recursive_search(source_dict(source_dict[k], lookup_value, deep))
        if isinstance(v, list):
            deep += 1
            for i in v:
                if i == lookup_value:
                    return {'val': lookup_value, 'parent': k, 'deep': deep}
        if isinstance(v, str) and v == lookup_value:
            deep +=1
            return {'val': lookup_value, 'parent': k, 'deep': deep}




""" Source dict """
def get_source_dict():
    return {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Alex',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark']  # deep 6
                                    }
                                ]
                            }
                        }
                    ]
                },
            },
            'key8': 'Robert'  # deep 1
        }
    }

""" Test """
source_dict = get_source_dict()
values = [
    ("Alex", {'val': 'Alex', 'parent': 'key3', 'deep': 1}),
    ("Mary", {'val': 'Mary', 'parent': 'key5', 'deep': 2}),
    ('Duke', {'val': 'Duke', 'parent': 'key7', 'deep': 3}),
    ('Mark', {'val': 'Mark', 'parent': 'key10', 'deep': 6})
]

for lookup_value, expected_result in values:
    result = recursive_search(source_dict, lookup_value)
    #assert result == expected_result, f"{result} != {expected_result}"
    print(result)