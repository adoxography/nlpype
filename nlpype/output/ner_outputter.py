from nlpype.output.outputter import Outputter


class NEROutputter(Outputter):
    def print(self, document):
        builder = []
        mentions = {mention.index - 1: mention for mention in document.entity_mentions()}
        tokens = document.tokens()
        index = 0
        while index < len(tokens):
            if index in mentions:
                mention = mentions[index]
                builder.append(mention.tag())
                builder.append(' ')
                index += len(mention)
            else:
                builder.append(tokens[index].full())
                index += 1
        return ''.join(builder)

