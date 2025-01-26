import json

class TqlCommand:

    def __init__(self, tql_command):
        self.__tql_command = tql_command

    def get_tql_command(self):

        return self.__tql_command

class TqlCommands:

    def __init__(self, tql_commands):
        
        self.__list_of_tql_commands = tql_commands

    def get_tql_commands(self):
        
        return self.__list_of_tql_commands
        
