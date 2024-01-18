"""
Из файла info.yaml выведите имя и id Ливерпуля
"""
import yaml
from pprint import pprint
with open('info.yaml') as yamlfile:
    reader = yaml.safe_load(yamlfile)
    pprint(f'name: {reader[0]["name"]}; id: {reader[0]["id"]}')