#Text Data Preprocessing Lib
import json
import pickle
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


words = []
classes = []
word_tags_list = []
train_data_file = open("intents.json").read()
intents = json.loads(train_data_file)
ignore_words = ["?", ",", ".", "'s", "'m"]


 

# function for appending stem words
def get_stem_words(words, ignore_words):
    
    stem_words = []
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stem_words.append(w)
        
        print(stem_words)

wordsList = ["Running", "walking", "sleeping", "dancing", "writing"]
get_stem_words(wordsList, ignore_words)

for intent in intents['intents']:
    
        # Add all words of patterns to list
        for pattern in intent['patterns']:            
            pattern_word = nltk.word_tokenize(pattern)            
            words.extend(pattern_word)                      
            word_tags_list.append((pattern_word, intent['tag']))
        # Add all tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            stem_words = get_stem_words(words, ignore_words)

print(stem_words)
print(word_tags_list[0]) 
print(classes)   

#Create word corpus for chatbot
def create_bot_corpus(stem_words, classes):

    stem_words = sorted(list(stem_words))
    classes = sorted(list(set(classes)))

    pickle.dump(stem_words, open('words.pkl','wb'))
    pickle.dump(classes, open('classes.pkl','wb'))

    return stem_words, classes

stem_words, classes = create_bot_corpus(stem_words,classes)  

print(stem_words)
print(classes)


    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot

