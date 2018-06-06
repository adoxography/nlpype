from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreToken


with describe('CoreSentence') as self:
    with before.all:
        self.parser = StanfordCoreNLP(annotators='ssplit')
        document = self.parser.annotate('This is a sentence. This is another.')
        self.sentences = document.sentences()

    with it('has a list of tokens'):
        tokens = self.sentences[0].tokens()
        expect(all(isinstance(token, CoreToken) for token in tokens)).to(be_true)

    with it('can access tokens by index'):
        expect(str(self.sentences[0][3])).to(equal('sentence'))

    with it('can set tokens by index'):
        document = self.parser.annotate('This is a old sentence.')
        sentence = document[0]
        sentence[3] = 'new'
        expect(str(sentence[3])).to(equal('new'))

    with it('can set a slice of tokens by index'):
        document = self.parser.annotate('This is a very long sentence.')
        sentence = document[0]
        sentence[3:5] = 'short'
        phrase = ''.join(token.full() for token in sentence[3:5])
        expect(phrase).to(equal('short '))

