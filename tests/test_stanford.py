from mamba import *
from expects import *
from nlpype.stanford import StanfordCoreNLP
import jpype


with description('StanfordCoreNLP') as self:
    with it('loads an instance of CoreNLP'):
        parser = StanfordCoreNLP(annotators='tokenize')
        expect(str(type(parser._pipeline))).to(equal("<class 'jpype._jclass.edu.stanford.nlp.pipeline.StanfordCoreNLP'>"))

