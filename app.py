import json

from flask import Flask, render_template, request
import indicoio

app = Flask(__name__)


@app.route('/')
def index():
    '''Shows index page at localhost:5000'''
    return render_template('index.html')


@app.route('/crunch', methods=['POST'])
def send_to_indico():
    '''
    This route handles the server's response when
    you post data to localhost:5000/crunch through
    the form on index.html
    '''

    tweets_csv_string = request.form.get('tweets')
    csv_list = tweets_csv_string.replace('\r', '').splitlines()

    if len(csv_list) > 40:
        csv_list = csv_list[:40]

    tweet_list = []
    for csv_tweet in csv_list:
        tweet_only = csv_tweet.split(',')[2:]
        tweet_list.append(','.join(tweet_only))

    tweet_list = tweet_list[::-1]

    tweet_scores = indicoio.batch_sentiment(tweet_list, api_key="YOUR_API_KEY")
    return json.dumps({'scores': tweet_scores, 'tweets': tweet_list})  # dumps converts res to a JSON object


if __name__ == '__main__':
    app.run(debug=True)
