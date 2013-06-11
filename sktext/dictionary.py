import math


def bow(xs):
    counts = dict()
    for x in xs:
        counts[x] = counts.get(x, 0) + 1
    return counts


class Dictionary(object):
    def __init__(self):
        # self.current_index = 0
        self.index2token = []  # mapping from indices to strings
        self.token2index = dict()  # mapping from strings to ints
        self.term_counts = []  # mapping from indices to counts (ints)
        self.document_counts = []  # mapping from indices to counts (maximum one per doc)

    def add(self, tokens):
        '''Adds tokens to the dictionary as needed, and returns list of indices, converted.
        Increments (document & term) counts, too.'''
        indices = [self.add_one(token) for token in tokens]

        for index in set(indices):
            self.document_counts[index] += 1

        return indices

    def add_one(self, token):
        index = self.token2index.get(token)
        if index is None:
            index = len(self.index2token)
            self.token2index[token] = index
            self.index2token.append(token)
            self.term_counts.append(1)
            self.document_counts.append(0)
        else:
            self.term_counts[index] += 1
        return index

    def indexify(self, tokens):
        return [self.token2index.get(token, None) for token in tokens]

    def resolve(self, indices):
        return [self.index2token[index] for index in indices]

    def __str__(self):
        return '''
            token2index %(token2index)s
            index2token %(index2token)s
            term_counts %(term_counts)s
        ''' % dict(
            token2index=self.token2index.items()[:10],
            index2token=self.index2token[:10],
            term_counts=self.term_counts[:10])

    def tfidf(self, documents):
        """ Apply TermFrequency(tf)*inverseDocumentFrequency(idf) for each matrix element.
        This evaluates how important a word is to a document in a corpus

        params:
        @documents = [[doc_1_token_1, doc_1_token_2, ...], [doc_2_token_1, doc_2_token_2, ...], ...]

        With a document-term matrix: matrix[x][y]
        tf[x][y] = frequency of term y in document x / frequency of all terms in document x
        idf[x][y] = log( abs(total number of documents in corpus) / abs(number of documents with term y)  )
        Note: This is not the only way to calculate tf*idf
        """

        tfidf_documents = []
        document_count = len(documents)
        for tokens in documents:
            tfidf_document = dict()
            for token, tf in bow(tokens).items():
                idf = math.log(float(document_count) / self.document_counts[token])
                tfidf_document[token] = tf * idf

            tfidf_documents.append(tfidf_document)
        return tfidf_documents
