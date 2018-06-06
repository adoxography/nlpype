from abc import ABCMeta

from nlpype.objects import cache
from nlpype.objects.core_token import CoreToken


class HasTokens(metaclass=ABCMeta):
    """
    Module for CoreNLP objects that have tokens
    """
    def __getitem__(self, index):
        """
        Accesses a token by index

        :param index: The index of the token
        :type index: int
        :return: The token at the specified index
        :rtype: CoreToken
        """
        return self.tokens()[index]

    def __setitem__(self, index, word):
        """
        Sets the text of the token(s) at the given index

        :param index: Either an index of a token or a slice of tokens to set
        :type index: Union[int, slice]
        :param word: The text to set the first token in the range to
        :type word: str
        """
        if isinstance(index, slice):
            start = index.start
            end = index.stop

            if start is None:
                start = 0
            if end is None:
                end = len(self)
        else:
            start = end = index

        self[start].text = word

        for token in self[start+1:end]:
            token.text = ''
        for token in self[start:end-1]:
            token.no_space()

    @cache
    def tokens(self):
        """
        Retrieves the tokens contained in this object

        :rtype: list of CoreToken
        """
        return [CoreToken(token, self._pipeline) for token in self._base.tokens()]

    def __len__(self):
        return len(self.tokens())

