from mamba import *
from expects import *
import jpype

from nlpype.stanford import StanfordCoreNLP
from nlpype.objects import CoreDocument

with description('StanfordCoreNLP') as self:
    
    with before.all:
        self.parser = StanfordCoreNLP(annotators='tokenize')

    with it('loads an instance of CoreNLP'):
        expect(str(type(self.parser._pipeline))).to(equal("<class 'jpype._jclass.edu.stanford.nlp.pipeline.StanfordCoreNLP'>"))

    with it('annotates a string'):
        document = self.parser.annotate('The quick brown fox jumps over the lazy dog')
        expect(document).to(be_a(CoreDocument))
