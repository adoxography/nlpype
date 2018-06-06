from nlpype.java import jvm, corenlp, util
from nlpype.objects import CoreDocument


class StanfordCoreNLP:
    """ Wraps a Java StanfordCoreNLP pipeline """

    def __init__(self, **kwargs):
        """
        Initializes a CoreNLP pipeline

        :param props: The properties to initialize the pipeline with
        :type props: dict of str, str
        """
        jvm.boot()

        props = util.Properties()
        for k, v in kwargs.items():
            props.setProperty(k, v)
        
        self._pipeline = corenlp.pipeline.StanfordCoreNLP(props)

    def annotate(self, text):
        document = corenlp.pipeline.CoreDocument(text.replace('\n', ' '))
        self._pipeline.annotate(document)
        return CoreDocument(document)

