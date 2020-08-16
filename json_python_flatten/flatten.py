#  Copyright (c) 2020.  by Dheeraj Gupta.
#  This is part of json_flatten project.
#  Project: json_flatten
#  Module:
#  File: flatten.py
#  Author: Dheeraj Gupta
#  Description : tbd

# Global import
from itertools import chain, starmap


# Main Code


def flatten(dictionary):
    """
        Flatten a nested dictionary structure

    >>> flatten({'abc': {'a': 24, 'b': {'b1': {'size': 3, 'out': 'Nope'}, 'size': True}}, 'xyz': {'x': {'word': 8}, 'y': -1, 'z': 26}, 'pqr': {'pq': [0, None, 2.0, 3.0], 'r': None}})
    {'abc[a]': 24, 'abc[b][b1][size]': 3, 'abc[b][b1][out]': 'Nope', 'abc[b][size]': True, 'xyz[x][word]': 8, 'xyz[y]': -1, 'xyz[z]': 26, 'pqr[pq][0]': 0, 'pqr[pq][1]': None, 'pqr[pq][2]': 2.0, 'pqr[pq][3]': 3.0, 'pqr[r]': None}

    """

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                if type(value) == list:
                    for k, v in enumerate(value):
                        yield parent_key + '[' + key + ']' + '['+str(k)+']', v
                else:
                    yield parent_key + '['+key+']', value
    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break
    return dictionary