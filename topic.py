from gensim import corpora, models
import re

def extract_topics(text_list, num_topics=1):
    # Preprocessing and LDA Topic Modeling
    processed = [re.sub(r'[^a-zA-Z\s]', '', doc.lower()).split() for doc in text_list]
    dictionary = corpora.Dictionary(processed)
    corpus = [dictionary.doc2bow(doc) for doc in processed]
    
    if not corpus: return "No Topics Found"
    
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    topics = lda.show_topic(0, topn=3)
    return ", ".join([word for word, prob in topics])


