class Annotator:
    def __init__(self, name, requires):
        self.name = name
        self.requires = requires

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        if isinstance(other, Annotator):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False


TOKENIZE = Annotator('tokenize', [])
SSPLIT   = Annotator('ssplit', [TOKENIZE])
POS      = Annotator('pos', [])
LEMMA    = Annotator('lemma', [])
NER      = Annotator('ner', [])
ENTITY_MENTIONS = Annotator('entitymentions', [TOKENIZE, SSPLIT, POS, LEMMA, NER])
ANNOTATORS = [TOKENIZE, SSPLIT, POS, LEMMA, NER, ENTITY_MENTIONS]


def get_annotator(name):
    return next((annotator for annotator in ANNOTATORS if annotator.name == name), None)


def sort_annotators(unsorted):
    return [annotator for annotator in ANNOTATORS if annotator in unsorted]
