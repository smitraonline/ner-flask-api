import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

# word tokenize and pos tagging
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

#sent = preprocess(ex)
#print(sent)

#named entity chunking
def process_content():
    try:
       tagged =  preprocess(ex)
       namedEnt = nltk.ne_chunk(tagged)
       print(namedEnt)
    finally:
        pass
# test
#process_content()

# tokenize handler for api
def tokenize(data):
    try:
       tagged =  preprocess(data)
       data = tagged
    finally:
        return data

# data = tokenize(ex)
# print(data)


# anonymize handler for api
def anonymize_ne(data):
    try:
        # chunk
        tagged =  preprocess(data)
        namedEnt = nltk.ne_chunk(tagged)

        # identify
        named_entities = []
        for tagged_tree in namedEnt:
            if hasattr(tagged_tree, 'label'):
               entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
               entity_type = tagged_tree.label()
               named_entities.append((entity_name, entity_type))
        
        # replace
        for ent in named_entities:
            data = data.replace(ent[0], '<' + ent[1] + '>')
    finally:
        return data
        pass


# name anonymize handler for api.
def anonymize(data):
    return anonymize_ne(data)

# data = sanitize(ex)
# print(data)