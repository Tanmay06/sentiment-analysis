#!/usr/bin/env python
# coding: utf-8

from SentimentAnalysis.ProcessWords import review_to_wordlist, get_data_ready
from sklearn.externals import joblib
from json import load

model = joblib.load("SentimentAnalysis/models/model-0.69-0.003-50.joblib")

with open("SentimentAnalysis/dictionary/word2index.json","r") as json_file:
	word2index = load(json_file)

def predict_sentiment(text):

	processed_text = review_to_wordlist(text)

	input_text_array = get_data_ready([processed_text], word2index) 

	prediction = model.predict(input_text_array)

	return prediction[0]
