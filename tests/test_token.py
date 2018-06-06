from mamba import *
from expects import *

from nlpype import StanfordCoreNLP


with describe('CoreToken') as self:
    with before.all:
        parser = StanfordCoreNLP(annotators='ssplit')
        document = parser.annotate('This is a sentence.')
        self.tokens = document[0].tokens()

    with it('yields its underlying string with str'):
        token = self.tokens[1]
        expect(str(token)).to(equal('is'))

    with it('yields its underlying string with text'):
        token = self.tokens[1]
        expect(token.text).to(equal('is'))

    with it('sets its underlying string with text'):
        token = self.tokens[1]
        token.text = 'hello'
        expect(token.text).to(equal('hello'))

