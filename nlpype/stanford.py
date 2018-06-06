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
        """
        Annotates a document with the underlying pipeline

        :param text: The document to annotate
        :type text: str
        :return: An annotated CoreNLP document
        :rtype: CoreDocument
        """
        document = corenlp.pipeline.CoreDocument(text.replace('\n', ' '))
        self._pipeline.annotate(document)
        return CoreDocument(document)

