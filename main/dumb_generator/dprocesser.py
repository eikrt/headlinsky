import random
def get_random_words(words, length):
    random_words = []
    for x in range(length):
        random_words.append(words[random.randint(0,len(words))])
    return random_words

def get_headline(source_material):
    words = []
    for material in source_material:
        for s in material.split():
            words.append(s)
    
    return(" ".join(get_random_words(words, 6)))
