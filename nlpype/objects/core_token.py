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

    def _get_after(self):
        return self._base.after()

    def _set_after(self, value):
        self._base.setAfter(value)

    def _get_tag(self):
        return self._base.tag()

    def _set_tag(self, tag):
        self._base.setTag(tag)

    text = property(_get_text, _set_text)
    after = property(_get_after, _set_after)
    tag = property(_get_tag, _set_tag)

    def space(self):
        self.after = ' '

    def no_space(self):
        self.after = ''

    def full(self):
        return self.text + self.after

