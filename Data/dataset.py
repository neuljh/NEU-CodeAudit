class Dataset:
    def __init__(self, variables, macros, functions):
        self.variables = variables
        self.macros = macros
        self.functions = functions

    def get_variables(self):
        return self.variables

    def set_variables(self, variables):
        self.variables = variables

    def get_macros(self):
        return self.macros

    def set_macros(self, macros):
        self.macros = macros

    def get_functions(self):
        return self.functions

    def set_functions(self, functions):
        self.functions = functions