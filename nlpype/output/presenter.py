import sys
from abc import ABCMeta, abstractmethod


class Presenter(metaclass=ABCMeta):
    def __init__(self, stream=None):
        self._stream = stream or sys.stdout

    @abstractmethod
    def convert(self, document):
        pass

    def print(self, document):
        text = self.convert(document)
        self._stream.write(text)
        self._stream.flush()

