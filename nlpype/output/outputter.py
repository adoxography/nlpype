import sys
from abc import ABCMeta, abstractmethod


class Outputter(metaclass=ABCMeta):
    def __init__(self, stream=None):
        self._stream = stream

    @abstractmethod
    def print(self, document):
        pass

