from abc import ABCMeta

from nlpype.objects import cache
from nlpype.objects.core_token import CoreToken


class HasTokens(metaclass=ABCMeta):
    """
    Module for CoreNLP objects that have tokens
    """
    def __getitem__(self, index):
        return self.tokens()[index]

    # def __setitem__(self, index, word):
    #     if 

    @cache
    def tokens(self):
        return [CoreToken(token, self._pipeline) for token in self._base.tokens()]

