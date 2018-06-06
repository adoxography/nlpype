from nlpype.objects import CoreObject, cache
from nlpype.objects.core_token import CoreToken


class CoreMention(CoreObject):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreEntityMention
    """
    @cache
    def tokens(self):
        return [CoreToken(token, self._pipeline) for token in self._base.tokens()]

