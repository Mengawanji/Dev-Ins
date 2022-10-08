# with open('output.text','w') as fp:
#     pass

# f = open('output.txt', 'w')
# for i in range(10):
#     f.write("this is line: %i\n"%i)
# f.close()

import json


with open('index.py','w') as fp:
    pass

f = open('index.py','w')

f.close()

family = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
json_file = "file.json"

with open(json_file, 'w') as fp:
    json.dump(family, fp, indent = 2, sort_keys=True)

