from mamba import *
from expects import *

from nlpype import StanfordCoreNLP


with describe('CoreToken') as self:
    with before.all:
        parser = StanfordCoreNLP(annotators='entitymentions')
        self.document = parser.annotate('This is a sentence. John likes cats.')
        self.tokens = self.document[0].tokens()

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

    with it('returns its after attribute'):
        token = self.tokens[1]
        expect(token.after).to(equal(' '))

    with it('sets its after attribute'):
        token = self.tokens[1]
        token.after = 'x'
        expect(token.after).to(equal('x'))

    with it('sets its after attribute to the empty string'):
        token = self.tokens[1]
        token.no_space()
        expect(token.after).to(equal(''))

    with it('sets its after attribute to a space'):
        token = self.tokens[3]
        token.space()
        expect(token.after).to(equal(' '))

    with it('returns the text and the string afterwords') :
        token = self.tokens[2]
        expect(token.full()).to(equal('a '))

    with it('gets its ner tag'):
        token = self.document[1][0]
        expect(token.ner).to(equal('PERSON'))

    with it('sets its ner tag'):
        token = self.document[1][0]
        token.ner = 'PLACE'
        expect(token.ner).to(equal('PLACE'))

    with it('raises an error if NER is accessed without the ner annotator'):
        parser = StanfordCoreNLP(annotators='ssplit')
        document = parser.annotate('This is a sentence. John likes cats.')
        token = document[1][0]
        expect(token._get_ner).to(raise_error(AttributeError))

