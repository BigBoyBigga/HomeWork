"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""
import json
import yaml
with open('character.json') as jsonfile:
    jsonreader = json.load(jsonfile)
with open("areg.yaml", 'w') as yamlfile:
    yaml.dump(jsonreader, yamlfile)