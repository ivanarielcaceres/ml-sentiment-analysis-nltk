from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from translate import Translator
from langdetect import detect
from pymongo import MongoClient
import pandas as pd
import langid
import textblob
import requests
import json 

app = Flask(__name__)
app.debug = True

#Configure MongoDB client
client = MongoClient('172.17.0.2', 27017)
db = client['twitterdb']
twitter_itaipu_db = db['sentiment_analysis']

def transl(text):
    to_lang = ['en', 'pt', 'es']
    response = {}
    try:
        from_lang =  textblob.TextBlob(text).detect_language()
        for lang in to_lang:
            translator = Translator(to_lang=lang, from_lang=from_lang)
            response[lang] = translator.translate(text)
        return json.dumps(response)
    except Exception as e:
        print(e)


@app.route('/healthz')
def healthz():
    return "it's alive"

@app.route('/translate', methods=['POST'])
def translate():
    params = request.get_json()
    to_lang = ['en', 'pt', 'es']
    text = params['text']
    response = transl(text)
    return response

@app.route('/sentiment', methods=['POST'])
def sentiment():
    params = request.get_json()
    text = params['text']
    translated = json.loads(transl(text))['en']
    analyzer = SentimentIntensityAnalyzer()
    response = ''
    try:
        vs = analyzer.polarity_scores(translated)
        params['translated'] = translated
        params['sentiment'] = str(vs)
        twitter_itaipu_db.insert(params)
        response = str(vs)
    except Exception as e:
        response = str(e)
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
