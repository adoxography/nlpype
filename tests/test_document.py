from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreSentence


with description('CoreDocument') as self:
    with before.all:
        self.parser = StanfordCoreNLP(annotators='tokenize, ssplit')

    with it('raises an error if sentences are accessed without the ssplit annotator'):
        parser = StanfordCoreNLP(annotators='tokenize')
        document = parser.annotate('This is a sentence. This is another.')
        expect(document.sentences).to(raise_error(AttributeError))

    with it('contains a list of CoreSentence objects'):
        document = self.parser.annotate('This is a sentence. This is another.')
        expect(all([isinstance(sent, CoreSentence) for sent in document])).to(be_true)

