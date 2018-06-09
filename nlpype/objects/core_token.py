from nlpype.objects import CoreObject, cache
from nlpype.annotators import NER


class CoreToken(CoreObject):
    """
    Wraps an edu.stanford.nlp.ling.CoreLabel
    """
    def __str__(self):
        return self.text

    def _get_text(self):
        return self._base.originalText()

    def _set_text(self, value):
        return self._base.setOriginalText(value)

    def _get_after(self):
        return self._base.after()

    def _set_after(self, value):
        self._base.setAfter(value)

    def _get_tag(self):
        return self._base.tag()

    def _set_tag(self, tag):
        self._base.setTag(tag)

    def _get_ner(self):
        if NER not in self._pipeline.annotators:
            raise AttributeError('This token was not parsed with named entity recognition.')
        return self._base.ner()

    def _set_ner(self, value):
        self._base.setNER(value)

    text = property(_get_text, _set_text)
    after = property(_get_after, _set_after)
    tag = property(_get_tag, _set_tag)
    ner = property(_get_ner, _set_ner)

    def space(self):
        self.after = ' '

    def no_space(self):
        self.after = ''

    def full(self):
        return self.text + self.after

