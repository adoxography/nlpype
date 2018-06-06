from nlpype.objects import CoreObject, cache
from nlpype.objects.has_tokens import HasTokens


class CoreMention(CoreObject, HasTokens):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreEntityMention
    """
    pass

