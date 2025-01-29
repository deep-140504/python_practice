import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
def antonyms_and_synonyms(word):
    # synsets = wn.synset(word)
    synsets = wn.synsets(word)
    synonyms = set()
    antonyms = set()
    for syn in synsets:
        for lemma in syn.lemmas(): 
            synonyms.add(lemma.name()) 
            for antonym in lemma.antonyms():
                antonyms.add(antonym.name()) 
    return list(synonyms), list(antonyms)

word = input("Please enter a word: ")
synonyms, antonyms = antonyms_and_synonyms(word)
print(synonyms)
print(antonyms)