from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreSentence, CoreMention


with description('CoreDocument') as self:
    with before.all:
        self.parser = StanfordCoreNLP(annotators='tokenize, ssplit, pos, lemma, ner, entitymentions')

    with it('raises an error if sentences are accessed without the ssplit annotator'):
        parser = StanfordCoreNLP(annotators='tokenize')
        document = parser.annotate('This is a sentence. This is another.')
        expect(document.sentences).to(raise_error(AttributeError))

    with it('contains a list of CoreSentence objects'):
        document = self.parser.annotate('This is a sentence. This is another.')
        expect(all(isinstance(sent, CoreSentence) for sent in document)).to(be_true)

    with it('raises an error if mentions are accessed without the entitymentions annotator'):
        parser = StanfordCoreNLP(annotators='tokenize')
        document = parser.annotate('Bob owns a car.')
        expect(document.entity_mentions).to(raise_error(AttributeError))

    with it('contains a list of CoreMention objects'):
        document = self.parser.annotate('Bob owns a car.')
        expect(all(isinstance(ment, CoreMention) for ment in document.entity_mentions())).to(be_true)

