import json
# file = open("my_data.json")
# data = file.read()

# print(type(data))
# print(data)
# file.close()

with open("my_data.json") as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    # print(type(json_data))
    for line in json_data:
        print(line)
        print(type(line))
    for line in json_data:
        print(type(line))
        print(line)
    id=line.get("id")
    name = line.get("name")
    print(id,name)

    