#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request, session
from SentimentAnalysis.PredictSentiment import predict_sentiment
import requests as rq

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/predict")
def predict():
	prediction_pict = {0:"negative.png",1:"positive.png"}
	
	sentence = request.args.get("sentence")
	prediction = predict_sentiment(sentence)

	session["sentence"] = sentence
	session["prediction"] = prediction
 
	return render_template("prediction.html",prediction_image = prediction_pict[prediction],prediction_text = sentence)

@app.route("/review")
def review():

	data = { "Status" : request.args.get("check") == "1", "Prediction" : session["prediction"] == "1",
	"Sentence" : session["sentence"], "Client" : requests.remote_addr }

	url = "https://sentibo-sentiment-analysis.firebaseio.com/reviews.json"

	r = rq.post(url, data = data) 

	return render_template("thanks.html")