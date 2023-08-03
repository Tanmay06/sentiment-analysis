#!/usr/bin/env python
# coding: utf-8

from json import loads

import joblib
import requests as rq

from SentimentAnalysis.processwords import review_to_wordlist, get_data_ready

class PredictSentiment:
	def __init__(self) -> None:
		self._load_model()
		self._load_dictionary()
		pass

	def _load_model(self):
		self.model = joblib.load("SentimentAnalysis/models/model-0.69-0.003-50.joblib")
		pass

	def _load_dictionary(self):
		url = "https://firebasestorage.googleapis.com/v0/b/sentibo-sentiment-analysis.appspot.com/o/dictionary%2Fword2index.json?alt=media&token=1f328386-4385-4a5a-840d-8e507cccf505"
		res = rq.get(url)
		self.word2index = loads(res.content)

	def predict_sentiment(self, text):

		processed_text = review_to_wordlist(text)

		input_text_array = get_data_ready([processed_text], self.word2index) 

		prediction = self.model.predict(input_text_array)

		return prediction[0]
