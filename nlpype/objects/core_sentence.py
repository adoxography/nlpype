from nlpype.objects import CoreObject
from nlpype.objects.has_tokens import HasTokens


class CoreSentence(CoreObject, HasTokens):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreSentence
    """
    def regenerate(self):
        return ''.join(token.full() for token in self.tokens())
