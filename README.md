# json_flatten
Flatten/unflatten the JSON object in python.

## Installation
```bash
pip install json_flatten
```

## Usages
### Flatten
```python
# Input Dict
input_dict = {
"abc": {"a": 24,
          "b": {"b1": {"size": 3,
                          "out": "Nope"},
                "size": True}},
"xyz": {"x": {"word": 8}, "y": -1, "z": 26},
"pqr": {"pq": [0, None, 2.0, 3.0],
          "r": None}
}
from json_python_flatten import flatten
print(flatten(dictionary=input_dict))
{
   "abc[a]":24,
   "abc[b][b1][size]":3,
   "abc[b][b1][out]":"Nope",
   "abc[b][size]":True,
   "xyz[x][word]":8,
   "xyz[y]":-1,
   "xyz[z]":26,
   "pqr[pq][0]":0,
   "pqr[pq][1]":"None",
   "pqr[pq][2]":2.0,
   "pqr[pq][3]":3.0,
   "pqr[r]":"None"
}
```

## Un-Flatten
```python
json_dict = {   
   "columns[0][data]":"0",
   "columns[0][name]":"",
   "columns[0][searchable]":"true",
   "columns[0][orderable]":"false",
   "columns[0][search][value]":"",
   "columns[0][search][regex]":"false",
   "order[0][column]":"1",
   "order[0][dir]":"asc",
   "start":"0",
   "length":"13",
   "search[value]":"jenkins",
   "search[regex]":"false",
   "searchPanes[group][0]":"Group 1",
   "searchPanes[platform][0]":"Window"
} 
from json_python_flatten import unflatten
print(unflatten(json_dict=json_dict))
{
   "columns":[
      {
         "data":"0",
         "name":"",
         "searchable":"true",
         "orderable":"false",
         "search":{
            "value":"",
            "regex":"false"
         }
      }
   ],
   "order":[
      {
         "column":"1",
         "dir":"asc"
      }
   ],
   "start":"0",
   "length":"13",
   "search":{
      "value":"jenkins",
      "regex":"false"
   },
   "searchPanes":{
      "group":[
         "Group 1"
      ],
      "platform":[
         "Window"
      ]
   }
}
```
