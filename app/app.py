#!/usr/bin/env python
# coding: utf-8

import os
from json import dumps
from datetime import datetime

from flask import Flask, render_template, request
from SentimentAnalysis.predictsentiment import PredictSentiment
import requests as rq

app = Flask(__name__)

@app.route("/")
def index():
	
	return render_template("index.html")

@app.route("/predict")
def predict():

	prediction_pict = {0:"negative.png",1:"positive.png"}
	
	prediction_text = {0:"Your reponse seems negative.",1:"Your response seems positive."}

	sentence = request.args.get("sentence")
	prediction = predict_sentiment(sentence)

	return render_template("prediction.html",prediction_image = prediction_pict[prediction],
		prediction_text = prediction_text[prediction], prediction = str(prediction), sentence = sentence)

@app.route("/review")
def review():

	data = { "Status" : request.args.get("check") == "1", "Prediction" : request.args.get("prediction") == "1",
	"Sentence" : request.args.get("sentence"), "Client" : request.remote_addr, "TimeStamp" : str(datetime.now()) }

	url = "https://sentibo-sentiment-analysis.firebaseio.com/reviews.json"

	res = rq.post(url, data = dumps(data)) 
	

	return render_template("thanks.html")


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 3000))
	app.run(host='0.0.0.0',port=port)