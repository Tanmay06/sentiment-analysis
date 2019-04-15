#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
from SentimentAnalysis.PredictSentiment import predict_sentiment

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/predict")
def predict():
	prediction_pict = {0:"negative.png",1:"positive.png"}
	
	sentence = request.args.get("sentence")
	prediction = predict_sentiment(sentence)

	return render_template("prediction.html",prediction_image = prediction_pict[prediction],prediction_text = sentence)

@app.route("/review")
def review():
	return