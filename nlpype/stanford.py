import re

from nlpype.ner import tag_named_entities
from nlpype.javalib import jvm, corenlp, util
from nlpype.objects import CoreDocument
from nlpype.util.loading import Loader, StreamReader
from nlpype.annotators import get_annotator, sort_annotators


class StanfordCoreNLP:
    """ Wraps a Java StanfordCoreNLP pipeline """

    def __init__(self, corenlp_dir='/opt/stanford-corenlp/latest', **kwargs):
        """
        Initializes a CoreNLP pipeline

        :param props: The properties to initialize the pipeline with
        :type props: dict of str, str
        """
        jvm.boot(corenlp_dir)
        self._set_props(kwargs)

        props = util.Properties()
        for k, v in self._props.items():
            props.setProperty(k, v)

        reader = StreamReader(jvm.stderr, pattern=r'Adding annotator.*')
        with Loader('Loading Stanford CoreNLP...', reader):
            self._pipeline = corenlp.pipeline.StanfordCoreNLP(props)

    def _set_props(self, props):
        if 'annotators' in props:
            if isinstance(props['annotators'], str):
                annotators = re.split('[\s,]', props['annotators'])
            else:
                annotators = props['annotators']
        else:
            annotators = ['tokenize']
        annotators = [get_annotator(name) for name in annotators]

        requirements = []
        for annotator in annotators:
            if annotator:
                requirements += annotator.requires

        annotators = set(requirements + annotators)
        props['annotators'] = ','.join(
            [annotator.name for annotator in sort_annotators(annotators)]
        )
        self._props = props

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

    def resolve_pronouns(self, text):
        document = self.annotate(text)
        document.resolve_pronouns()
        return document.regenerate()

    def tag_named_entities(self, text, **kwargs):
        return tag_named_entities(text, self, **kwargs)

    @property
    def annotators(self):
        """
        Retrieves the annotators this pipeline was initialized with
        """
        if 'annotators' in self._props:
            return re.split('[\s,]', self._props['annotators'])
        return []
