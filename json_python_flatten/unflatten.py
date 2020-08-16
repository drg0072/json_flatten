#  Copyright (c) 2020.  by Dheeraj Gupta.
#  This is part of json_flatten project.
#  Project: json_flatten
#  Module:
#  File: unflatten.py
#  Author: Dheeraj Gupta
#  Description : tbd

# Global import

# Main Code


json = {'draw': '3', 'columns[0][data]': '0', 'columns[0][name]': '', 'columns[0][searchable]': 'true', 'columns[0][orderable]': 'false', 'columns[0][search][value]': '', 'columns[0][search][regex]': 'false', 'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '13', 'search[value]': 'jenkins', 'search[regex]': 'false', 'searchPanes[group][0]': 'Group 1', 'searchPanes[platform][0]': 'Window', '_': '1597573303858'}

def unflatten(json_dict):
    """
        Convert the JSON Flat dictionary into nested one.

    >>> unflatten({'draw': '3', 'columns[0][data]': '0', 'columns[0][name]': '', 'columns[0][searchable]': 'true', 'columns[0][orderable]': 'false', 'columns[0][search][value]': '', 'columns[0][search][regex]': 'false', 'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '13', 'search[value]': 'jenkins', 'search[regex]': 'false', 'searchPanes[group][0]': 'Group 1', 'searchPanes[platform][0]': 'Window', '_': '1597573303858'})
    {'draw': '3', 'columns': [{'data': '0', 'name': '', 'searchable': 'true', 'orderable': 'false', 'search': {'value': '', 'regex': 'false'}}], 'order': [{'column': '1', 'dir': 'asc'}], 'start': '0', 'length': '13', 'search': {'value': 'jenkins', 'regex': 'false'}, 'searchPanes': {'group': ['Group 1'], 'platform': ['Window']}, '_': '1597573303858'}

    """
    import re
    dictionary = {}
    for key, value in json_dict.items():
        temp_dict = dictionary
        tokens = re.findall(r'\w+', key)
        for count, (index, next_token) in enumerate(zip(tokens, tokens[1:] + [value]), 1):
            value = next_token if count == len(tokens) else [] if next_token.isdigit() else {}
            if isinstance(temp_dict, list):
                index = int(index)
                while index >= len(temp_dict):
                    temp_dict.append(value)
            elif index not in temp_dict:
                temp_dict[index] = value
            temp_dict = temp_dict[index]
    return dictionary