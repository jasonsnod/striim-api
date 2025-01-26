import json
from enum import Enum

class CommandTypes(Enum):

    CREATE = 'create'
    CREATE_OR_REPLACE = 'create or replace'
    ALTER = 'alter'
    END = 'end'
    DEPLOY = 'deploy'
    UNDEPLOY = 'undeploy'
    QUIESCE = 'quiesce'
    RUN_TQL_FILE = '\@'
    DESCRIBE = 'describe'
    EXPORT = 'export'
    HISTORY = 'history'
    IMPORT = 'import'
    LIST = 'list'
    LOAD = 'load'
    UNLOAD = 'unload'
    METER = 'meter'
    MONITOR = 'mon'
    PREVIEW = 'preview'
    REPORT = 'report'
    RESUME = 'resume'
    SELECT = 'select'
    SHOW = 'show'
    START = 'start'
    STATUS = 'status'
    STOP = 'stop'
    USAGE = 'usage'

class TqlCommand:
    
    def __init__(self, tql_command):
        
        tql_command_as_json = self.__tql_command_from_json(tql_command)
        if not tql_command_as_json:
            self.__full_tql_command = tql_command
        else:
            self.__full_tql_command = tql_command_as_json

        if 'command' in self.__full_tql_command:
            self.__command_type = CommandTypes(self.__full_tql_command["command"])
        
        if 'component_type' in self.__full_tql_command:
            self.__component_type = self.__full_tql_command["component_type"]
        
        if 'component_namespace' in self.__full_tql_command:
            self.__component_namespace = self.__full_tql_command["component_namespace"]
            
        if 'component_name' in self.__full_tql_command:
            self.__component_name = self.__full_tql_command["component_name"]

        if 'adapter_type' in self.__full_tql_command:
            self.__adapter_type = self.__full_tql_command["adapter_type"]

        if 'arguments' in self.__full_tql_command:
            self.__arguments = self.__full_tql_command["arguments"]

        if 'parameters' in self.__full_tql_command:
            self.__parameters = self.__full_tql_command["parameters"]

    def __tql_command_from_json(self, tql_command):

        try:
            return json.load(tql_command)

        except ValueError as error:

            print(error)
            print('TQL command is not of json, so can treat the argument as a Python object already deserialized from json format')
            return False
    


    def get_full_tql_command(self):

        return self.__tql_command
    
    def get_full_tql_string_command(self):

        return


class TqlCommands:

    def __init__(self, tql_commands:list):
        
        for tql_command in tql_commands:
    
            if not isinstance(TqlCommand, tql_command):
                print('Could not add this command to the list of TQL commands as it is not of type TqlCommand.')
    
            self.__list_of_tql_commands.append(tql_command)
        
    def get_tql_commands(self):
        
        return self.__list_of_tql_commands
        
