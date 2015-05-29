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
    data = request.form.get('text')
    api = request.form.get('api')

    indimodel = getattr(indicoio, api)  # grabs the appropriate method
    res = indimodel(data, api_key="YOUR_API_KEY")
    return json.dumps(res)  # dumps converts res to a JSON object


if __name__ == '__main__':
    app.run(debug=True)
