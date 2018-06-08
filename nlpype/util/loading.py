import re
import sys
import threading
import time
import itertools


class Loader:
    """
    Context manager that displays a spinner using a separate thread until the
    task on the main thread has completed
    """

    """ The characters to use for the spinner """
    SPINNER = '⠁⠂⠄⡀⢀⠠⠐⠈'

    def __init__(self, init, message):
        """
        Initializes the Loader

        :param init: A message to display before the loading
        :type init: str
        :param message: A message to display next to the spinner
        :type message: Union[str or callable]
        """
        self._init = init
        self._message = message
        self._max_length = 0
        self._thread = threading.Thread(target=self._animate)
        self._done = False

    def __enter__(self):
        """ Starts up the spinner """
        if self._init:
            print(self._init, file=sys.stderr)
        self._thread.start()

    def __exit__(self, *exc):
        """ Terminates the spinner """
        self._done = True
        self.print('\rDone!')
        sefl.print('\n')

    def _animate(self):
        """ Displays a message along with a spinner """
        for c in itertools.cycle(self.SPINNER):
            if self._done:
                break
            message = "\r{}...{} ".format(self.get_message(), c)
            self.print(message)
            time.sleep(0.1)

    def get_message(self):
        """ Retrieves the message that should be displayed with the spinner """
        if callable(self._message):
            return self._message()
        return self._message

    def print(self, message):
        """
        Prints text to stdout, ensuring that it is long enough to cover any
        previous messages

        :param message: The message to print
        """
        sys.stderr.write(message.rjust(self._max_length))
        sys.stderr.flush()
        self.set_max_length(message)

    def set_max_length(self, message):
        """
        Updates the max length of messages that have been printed

        :param message: The newest message
        """
        self._max_length = max([self._max_length, len(message)])


class StreamReader:
    """ Retrieves the latest line from a file stream """

    def __init__(self, stream, pattern=None):
        """
        Initializes the StreamReader

        :param stream: The stream to read from
        :type stream: File
        :param pattern: A pattern to look for in the stream
        :type pattern: str or re.Pattern
        """
        self._stream = stream
        self._latest = ''

        if pattern and isinstance(pattern, str):
            self._pattern = re.compile(pattern)
        else:
            self._pattern = pattern

    def __call__(self):
        """ Retrieves the latest line from the stream matching the pattern """
        lines = [line.rstrip() for line in self._stream.readlines() if self._accept(line)]
        if lines:
            self._latest = self._format(lines[-1])
        return self._latest

    def _accept(self, line):
        """
        Checks if a line is accepted by the reader
        
        :param line: The line to check
        :type line: str
        :return: True if the line is non-empty and matches the pattern (if
                 applicable) and False otherwise
        """
        if line:
            if self._pattern:
                return self._pattern.search(line)
            return True
        return False

    def _format(self, line):
        """
        Formats a line to be displayed

        :param line: The line to format
        :type line: str
        :return: The formatted line
        :rtype: str
        """
        if self._pattern:
            return self._pattern.search(line)[0]
        return line

