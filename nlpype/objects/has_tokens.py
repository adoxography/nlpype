from abc import ABCMeta

from nlpype.objects import cache
from nlpype.objects.core_token import CoreToken


class HasTokens(metaclass=ABCMeta):
    @cache
    def tokens(self):
        return [CoreToken(token, self._pipeline) for token in self._base.tokens()]

