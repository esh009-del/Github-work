import yaml 

with open("my_data.yaml") as yaml_file:
    #yaml_data = yaml.load(yaml file , loader = SafeLoader)
    yaml_data = yaml.safe_load(yaml_file)
    print(type(yaml_data))
    print(yaml_data)
    
with open("new_data.yaml", "w") as file:
    yaml.dump(yaml_data , file , sort_keys = False)
