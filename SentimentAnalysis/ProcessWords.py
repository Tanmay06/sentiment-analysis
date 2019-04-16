#!/usr/bin/env python
# coding: utf-8

from nltk.stem import SnowballStemmer
import numpy as np
import re

def review_to_wordlist(review, remove_stopwords=False):
    # Clean the text, with the option to remove stopwords.
    
    # Convert words to lower case and split them
    words = review.lower().split()

    # Optionally remove stop words (true by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    
    review_text = " ".join(words)

    # Clean the text
    review_text = re.sub(r"@[A-Za-z0-9_]*", "", review_text)
    review_text = re.sub(r"[^A-Za-z0-9(),!.?\'\`]", " ", review_text)
    review_text = re.sub(r"\'s", "'s", review_text)
    review_text = re.sub(r"\'ve", "'ve", review_text)
    review_text = re.sub(r"n\'t", "'t", review_text)
    review_text = re.sub(r"\'re", "'re", review_text)
    review_text = re.sub(r"\'d", "'d", review_text)
    review_text = re.sub(r"\'ll", "'ll", review_text)
    review_text = re.sub(r",", " ", review_text)
    review_text = re.sub(r"\.", " ", review_text)
    review_text = re.sub(r"!", " ", review_text)
    review_text = re.sub(r"\(", " ", review_text)
    review_text = re.sub(r"\)", " ", review_text)
    review_text = re.sub(r"\?", " ", review_text)
    review_text = re.sub(r"\s{2,}", " ", review_text)
    
    words = review_text.split()
    
    #Shorten words to their stems
    stemmer = SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in words]
    
    review_text = " ".join(stemmed_words)
    
    # Return a list of words
    return review_text

def get_data_ready(input_data, word2index):
    
    coded_data = np.zeros((len(input_data),len(word2index)))
    i = 0
    for each in input_data:
        
        text = review_to_wordlist(each)
        
        for word in text.split(" "):
            
            if word in word2index:
                coded_data[i,word2index[word]] += 1
        
        i += 1
        
    return coded_data