import os

from nlpype.java import jvm, corenlp, util
from nlpype.objects import CoreDocument
from nlpype.util.io import stdout_redirected, merged_stderr_stdout


class StanfordCoreNLP:
    """ Wraps a Java StanfordCoreNLP pipeline """

    def __init__(self, **kwargs):
        """
        Initializes a CoreNLP pipeline

        :param props: The properties to initialize the pipeline with
        :type props: dict of str, str
        """
        jvm.boot()
        self._props = kwargs

        props = util.Properties()
        for k, v in kwargs.items():
            props.setProperty(k, v)
        
        with stdout_redirected(to=os.devnull), merged_stderr_stdout():
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
        return CoreDocument(document, self)

    @property
    def annotators(self):
        """
        Retrieves the annotators this pipeline was initialized with
        """
        if 'annotators' in self._props:
            return self._props['annotators']
        return []

