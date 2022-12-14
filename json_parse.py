from json import load
from os import getcwd

class JsonParse:
    def __init__(self):
        self.__commands = ""

    def get_commands_by_classification(self, classification):
        if getcwd()[len(getcwd()) - 5:len(getcwd())] == 'train':
            with open('../json/' + str(classification) + '.json', 'r', encoding='utf-8') as file:
                self.__commands = load(file)
        else:
            with open('json/' + str(classification) + '.json', 'r', encoding='utf-8') as file:
                self.__commands = load(file)
        return self.__commands