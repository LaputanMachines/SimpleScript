# coding=utf-8
"""Represents a SymbolTable meant for tracking variables."""

from bin.number import Number


class SymbolTable:
    """Keep track of all new variable names and their values."""

    def __init__(self, parent=None):
        """
        Initialize an empty dictionary for the symbol table
        as well as a copy of the parent's symbol table.
        :param parent: Parent SymbolTable instance.
        """
        self.symbols = dict()
        self.parent = parent

        # Special values in the language
        self.symbols['NULL'] = Number(0)
        self.symbols['TRUE'] = Number(1)
        self.symbols['FALSE'] = Number(0)

    def get(self, variable_name, default=None):
        """
        Get the variable value from the SymbolTable.
        :param variable_name: Name of variable whose value we wish to fetch.
        :param default: Default value to return.
        :return: The value of the requested variable in memory.
        """
        variable_value = self.symbols.get(variable_name, default)
        if variable_value is None and self.parent:
            variable_value = self.parent.get(variable_name, default)
        return variable_value

    def set(self, variable_name, variable_value):
        """
        Sets a variable with a specific value into the SymbolTable.
        :param variable_name: Name of the new variable in memory.
        :param variable_value: Value of the new variable.
        """
        self.symbols[variable_name] = variable_value

    def remove(self, variable_name):
        """
        Removes a variable from the SymbolTable.
        :param variable_name: Name of the variable to remove.
        """
        del self.symbols[variable_name]
