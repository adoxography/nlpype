from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreToken


with describe('CoreSentence') as self:
    with before.all:
        parser = StanfordCoreNLP(annotators='ssplit')
        document = parser.annotate('This is a sentence. This is another.')
        self.sentences = document.sentences()

    with it('has a list of tokens'):
        tokens = self.sentences[0].tokens()
        expect(all(isinstance(token, CoreToken) for token in tokens)).to(be_true)

