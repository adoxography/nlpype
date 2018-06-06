from nlpype.objects import CoreObject, cache
from nlpype.objects.core_token import CoreToken


class CoreSentence(CoreObject):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreSentence
    """
    def tokens(self):
        return [CoreToken(token, self._pipeline) for token in self._base.tokens()]

