from nlpype.objects import CoreObject, cache


class CoreDocument(CoreObject):
    def __getitem__(self, index):
        return self.sentences()[index]

    def __len__(self):
        return len(self.sentences())

    @cache
    def sentences(self):
        return list(self._base.sentences())

    @cache
    def coref_chains(self):
        return list(self._base.corefChains().values())

    @cache
    def entity_mentions(self):
        mentions = sorted(
            self._base.entityMentions(), key=lambda x: x.charOffsets().first()
        )
        return mentions

    @cache
    def quotes(self):
        return list(self._base.quotes())

