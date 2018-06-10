from nlpype.annotators import ENTITY_MENTIONS
from nlpype.output import NERPresenter


def tag_named_entities(text, parser, **kwargs):
    if ENTITY_MENTIONS not in parser.annotators:
        raise AttributeError('The parser was not initalized with the entity mentions annotator.')
    presenter = NERPresenter()
    document = parser.annotate(text)
    return presenter.convert(document, **kwargs)

