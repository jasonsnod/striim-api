import traceback

class StriimException(Exception):

    def __init__(self, error, *error_strings):
        return self.list_errors(error.args, *error_strings)
    
    def list_errors(*error_strings):
        return [*error_strings, f'{traceback.format_exc()}']
            
            