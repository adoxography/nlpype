from nlpype.output import Presenter


class NERPresenter(Presenter):
    def convert(self, document, tag_pronouns=False):
        builder = []
        mentions = {
            mention.index - 1: mention
            for mention in document.entity_mentions()
        }
        tokens = document.tokens()
        index = 0
        while index < len(tokens):
            if index in mentions:
                mention = mentions[index]

                if mention.is_possessive() and not tag_pronouns:
                    builder.append(mention.full())
                else:
                    builder.append(mention.xml())
                    builder.append(' ')

                index += len(mention)
            else:
                builder.append(tokens[index].full())
                index += 1
        return ''.join(builder)
