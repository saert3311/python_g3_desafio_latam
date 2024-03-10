from flask import Flask, render_template
from api_request import api_request

app = Flask(__name__)

@app.route('/')
def index():
    bird_list, bird_response = api_request('GET', 'https://aves.ninjas.cl/api/birds')
    return render_template('birds.html', bird_list=bird_list, bird_response=bird_response)