from nlpype.objects import CoreObject, cache
from nlpype.objects.has_tokens import HasTokens
from nlpype.annotators import COREF


class CoreMention(CoreObject, HasTokens):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreEntityMention
    """
    def canonical(self):
        if COREF not in self._pipeline.annotators:
            raise AttributeError
        return CoreMention(self._base.canonicalEntityMention().get(), self._pipeline)

    def _get_text(self):
        return ''.join([token.full() for token in self]).strip()

    def _set_text(self, value):
        self[:] = value

    text = property(_get_text, _set_text)

