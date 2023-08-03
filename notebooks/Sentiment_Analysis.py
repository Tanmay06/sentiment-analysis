#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

data = pd.read_csv("twitter-sentiment-analysis2/train.csv",  encoding = "ISO-8859-1")

total_count = Counter()
for each in data.SentimentText:
    each = review_to_wordlist(each)
    for word in each.strip().split(" "):
        total_count[word] += 1
total_count = {key:count for key,count in total_count.most_common() if count > 1}

vocab = set(total_count.keys())
word2index = {word:idx for idx,word in enumerate(vocab)}

thresh = int(0.2 * len(data))

train_x, train_Y = data.SentimentText.iloc[:thresh], data.Sentiment.iloc[:thresh]
test_x, test_Y = data.SentimentText.iloc[thresh:], data.Sentiment.iloc[thresh:]

epochs = 50
lr = 0.001
hidden_layer = (10)
alpha = 0.0001

model = MLPClassifier(activation="relu", hidden_layer_sizes=hidden_layer, learning_rate_init=lr, 
                    validation_fraction=0.25, solver = "adam", max_iter = epochs, 
                      verbose = True, alpha = alpha, learning_rate = "adaptive", early_stopping=True)

train_X = get_data_ready(train_x, word2index)

model.fit(train_X,train_Y)

test_X = get_data_ready(test_x, word2index)

test_X = get_data_ready(test_x, word2index)

score_test = model.score(test_X,test_Y)
score_test = round(score_test,2)

filename = f"models/model-{score_test}-{lr}-{epochs}.joblib"
joblib.dump(model,filename)


