from mamba import *
from expects import *

from nlpype import StanfordCoreNLP
from nlpype.objects import CoreToken


with describe('CoreMention') as self:
    with before.all:
        parser = StanfordCoreNLP(annotators='entitymentions')
        document = parser.annotate('John Doe likes his car.')
        self.mentions = document.entity_mentions()

    with it('has a list of tokens'):
        tokens = self.mentions[0].tokens()
        expect(all(isinstance(token, CoreToken) for token in tokens)).to(be_true)

