# sentiment-analysis-nltk
Predict sentiment score with automatic translate technique
Technologies:

1. Python flask
/sentiment
  -Example request
   {"text": "Please, tell me my sentiment"}
  
   -Example response
   {
       "text": "Please, tell me my sentiment",
       "sentiment": "{'compound': 0.6, 'neu': 0.1, 'pos': 0.56,' neg': 0
   }

/translate
    -Example request
    {"text": "Por favor, traducime al ingles, portugues"}
    
    -Example response
    {
        "text": "Por favor, traducime a 2 idiomas",
        "en": "Please, translate me in two language",
        "pt": "bla bla bla bla"
    
    


