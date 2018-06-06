from nlpype.objects import CoreObject, cache


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

    text = property(_get_text, _set_text)

