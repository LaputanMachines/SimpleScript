# coding = utf-8
"""Error representations for the SimpleScript backend."""

from bin.helpers import string_with_arrows


class Error:
    """Custom error handling for language."""

    def __init__(self, error_name, error_details, start_pos, end_pos):
        """
        Create an Error instance with custom details.
        :param error_name: Name of the error instance.
        :param error_details: Description of the error.
        :param start_pos: Starting position of the character.
        :param end_pos: Ending position of the stream.
        """
        self.error_name = error_name
        self.error_details = error_details
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __str__(self):
        return repr(self)

    def __repr__(self):
        """Pretty-print error message."""
        error_msg = '\nFile {}, on line {}\n'.format(self.start_pos.fn, self.start_pos.ln + 1)
        error_msg += '{}: {}'.format(self.error_name, self.error_details)
        error_msg += '\n' + string_with_arrows(self.start_pos.ftxt, self.start_pos, self.end_pos) + '\n'
        return error_msg


##################################################
# ALL POSSIBLE ERRORS DURING EXECUTION           #
# NO DOCSTRINGS BECAUSE ALL CLASSES ARE THE SAME #
##################################################

class IllegalCharError(Error):
    def __init__(self, details, start_pos, end_pos):
        super(IllegalCharError, self).__init__(self.__class__.__name__,
                                               'Illegal character in the stream ({})'.format(details),
                                               start_pos,
                                               end_pos)


class InvalidSyntaxError(Error):
    def __init__(self, details, start_pos, end_pos):
        super(InvalidSyntaxError, self).__init__(self.__class__.__name__,
                                                 'Invalid syntax in the stream ({})'.format(details),
                                                 start_pos,
                                                 end_pos)


class ActiveRuntimeError(Error):
    def __init__(self, details, start_pos, end_pos, context):
        super(ActiveRuntimeError, self).__init__(self.__class__.__name__,
                                                 'Runtime error encountered ({}).'.format(details),
                                                 start_pos,
                                                 end_pos)
        self.context = context

    def __repr__(self):
        error_msg = self.generate_traceback()
        error_msg += '{}\n'.format(self.error_details)
        error_msg += string_with_arrows(self.start_pos.ftxt, self.start_pos, self.end_pos) + '\n'
        return error_msg

    def generate_traceback(self):
        """
        Generates a string for the stacktrace based on Contexts.
        :return: String of the stacktrace of the runtime stream.
        """
        result = ''
        context = self.context
        position = self.start_pos
        while context:
            # Add result instead of using += because we wish to keep
            # the stack trace chronological when it's printed out
            result = 'File {}, line {}, in {}\n'.format(position.fn,
                                                        position.ln + 1,
                                                        context.display_name) + result
            position = context.parent_entry_pos
            context = context.parent_context
        return '\nTraceback (most recent call last):\n' + result


class ExpectedCharError(Error):
    def __init__(self, details, start_pos, end_pos):
        super(ExpectedCharError, self).__init__(self.__class__.__name__,
                                                'Expected Character ({})'.format(details),
                                                start_pos,
                                                end_pos)
