from flask import Flask, jsonify
from flask import abort, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

@app.route("/",methods=["GET"])
def hello():
  return "hello"

@app.route("/", methods=["POST"])
def sentiment_scores():
          sentence=request.json
          x = sentence["text"]
          # return "Hello"
        # Create a SentimentIntensityAnalyzer object. 
          sid_obj = SentimentIntensityAnalyzer() 
     
        # polarity_scores method of SentimentIntensityAnalyzer 
        # oject gives a sentiment dictionary. 
        # which contains pos, neg, neu, and compound scores. 
          sentiment_dict = sid_obj.polarity_scores(x) 

          print("Overall sentiment dictionary is : ", sentiment_dict) 
          print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
          print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
          print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    
          print("Sentence Overall Rated As") 
    
        # decide sentiment as positive, negative and neutral 
          if sentiment_dict['compound'] >= 0.05 : 
            return("Positive") 
    
          elif sentiment_dict['compound'] <= - 0.05 : 
            return("Negative") 
    
          else : 
            return("Neutral")

if __name__ == '__main__':
    app.run(port=3000)