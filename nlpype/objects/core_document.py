from nlpype.annotators import SSPLIT, ENTITY_MENTIONS, COREF
from nlpype.objects import CoreObject, cache
from nlpype.objects.core_sentence import CoreSentence
from nlpype.objects.core_mention import CoreMention
from nlpype.objects.core_token import CoreToken


class CoreDocument(CoreObject):
    """
    Wraps an edu.stanford.nlp.pipeline.CoreDocument
    """
    def __getitem__(self, index):
        """
        Retrieves a sentence in the document by index

        :param index: The index of the sentence
        :type index: int
        :return: The sentence at the given index
        """
        return self.sentences()[index]

    def __len__(self):
        """
        :return: The number of sentences in the document
        """
        return len(self.sentences())

    @cache
    def sentences(self):
        """
        Retrieves the sentences from the base document and converts them into
        a Python list

        :return: A list of sentences contained in the document
        """
        if SSPLIT not in self._pipeline.annotators:
            raise AttributeError(
                'This document was not parsed with sentence tokenization.'
            )
        return [
            CoreSentence(sent, self._pipeline)
            for sent in self._base.sentences()
        ]

    @cache
    def tokens(self):
        return [
            CoreToken(token, self._pipeline)
            for token in self._base.tokens()
        ]

    @cache
    def coref_chains(self):
        """
        Retrieves the coreference chains from the base document and converts
        them into a Python list

        :return: A list of coreference chains contained in the document
        """
        return list(self._base.corefChains().values())

    @cache
    def entity_mentions(self):
        """
        Retrieves the entities mentioned in the base document and converts them
        into a Python list

        :return: A list of entities mentioned in the document
        """
        if ENTITY_MENTIONS not in self._pipeline.annotators:
            raise AttributeError(
                'This document was not parsed with entity mention recognition.'
            )
        mentions = sorted(
            self._base.entityMentions(), key=lambda x: x.charOffsets().first()
        )
        return [CoreMention(mention, self._pipeline) for mention in mentions]

    @cache
    def quotes(self):
        """
        Retrieves the quotes contained in the base document and converts them
        into a Python list

        :return: A list of quotes contained in the document
        """
        return list(self._base.quotes())

    def resolve_pronouns(self):
        """
        Resolves all of the pronouns to their canonical mentions
        """
        if ENTITY_MENTIONS not in self._pipeline.annotators \
                or COREF not in self._pipeline.annotators:
            raise AttributeError(
                'This document was not parsed with entity mention recognition and coreference resolution.'
            )
        for mention in self.entity_mentions():
            text = str(mention.canonical())

            if len(mention) == 1 and mention[0].tag == 'PRP$':
                text += "'s"

            mention.text = text

    def regenerate(self, sep=''):
        return sep.join([sent.regenerate() for sent in self.sentences()])
