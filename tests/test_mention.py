from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreToken


with describe('CoreMention') as self:
    with before.all:
        self.parser = StanfordCoreNLP(annotators='entitymentions, coref')
        document = self.parser.annotate('John Doe likes his car.')
        self.mentions = document.entity_mentions()

    with it('has a list of tokens'):
        tokens = self.mentions[0].tokens()
        expect(all(isinstance(token, CoreToken) for token in tokens)).to(be_true)

    with it('discovers its canonical mention if the coref annotator is used'):
        mention = self.mentions[1]
        expect(str(mention.canonical())).to(equal('John Doe'))

    # with it('throws an error if the coref annotator is not used'):
    #     parser = StanfordCoreNLP(annotators='entitymentions')
    #     document = parser.annotate('John Doe likes his car')
    #     mention = document.entity_mentions()[1]
    #     expect(mention.canonical).to(raise_error(AttributeError))

    with it('retrieves its text'):
        mention = self.mentions[0]
        expect(mention.text).to(equal('John Doe'))

    with it('sets its text'):
        mention = self.mentions[0]
        mention.text = 'Bob Barker'
        expect(mention.text).to(equal('Bob Barker'))

    with it('retrieves its ner tag'):
        mention = self.mentions[0]
        expect(mention.ner).to(equal('PERSON'))

    with it('sets its tag'):
        mention = self.mentions[0]
        mention.ner = 'PLACE'
        expect(mention.ner).to(equal('PLACE'))

    with it('sets the tags of its children'):
        mention = self.mentions[0]
        mention.ner = 'PLACE'
        expect(all(token.ner == 'PLACE' for token in mention)).to(be_true)

