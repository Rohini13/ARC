from flask import Flask, jsonify
from flask import abort, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)
from flask import send_from_directory
from flask import render_template

@app.route("/",methods=["GET"])
def hello():
  return "hello"

@app.route("/submit")
def submit():
  #root_dir = os.path.dirname(os.getcwd())
  return render_template('submit.html')
  #return app.send_static_file('submit.html')


@app.route("/", methods=["POST"])
def sentiment_scores():
          sentence=request.json
          x = sentence["text"] 
          sid_obj = SentimentIntensityAnalyzer() 
      
          sentiment_dict = sid_obj.polarity_scores(x) 

          print("Overall sentiment dictionary is : ", sentiment_dict) 
          print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
          print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
          print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    
          print("Sentence Overall Rated As") 
    
          if sentiment_dict['compound'] >= 0.05 : 
           return("Positive") 
    
          elif sentiment_dict['compound'] <= - 0.05 : 
            return("Negative") 
    
          else : 
            return("Neutral")

if __name__ == '__main__':
    app.run(port=3000)
