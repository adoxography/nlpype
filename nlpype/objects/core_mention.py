from nlpype.objects import CoreObject, cache
from nlpype.objects.has_tokens import HasTokens
from nlpype.annotators import COREF


class CoreMention(CoreObject, HasTokens):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreEntityMention
    """
    def __init__(self, base, pipeline):
        self._ner = None
        super().__init__(base, pipeline)

    def canonical(self):
        if COREF not in self._pipeline.annotators:
            raise AttributeError
        return CoreMention(self._base.canonicalEntityMention().get(), self._pipeline)

    def _get_text(self):
        return ''.join([token.full() for token in self]).strip()

    def _set_text(self, value):
        self[:] = value

    def _get_ner(self):
        if self._ner is None:
            self._ner = self._base.entityType()
        return self._ner

    def _set_ner(self, value):
        self._ner = value
        for token in self.tokens():
            token.ner = value

    text = property(_get_text, _set_text)
    ner = property(_get_ner, _set_ner)

