#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
from SentimentAnalysis.PredictSentiment import predict_sentiment

app = Flask(__name__)

@app.route("/")
def index():
	return "hello world"

@app.route("/analyse")
def analyse():

	return 