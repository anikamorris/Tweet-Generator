from flask import Flask, render_template, request, redirect, url_for
from histogram import list_of_lists_histogram, file_or_string
from stochastic_sampling import get_total_weight, random_weighted_word, get_sentence
import random

app = Flask(__name__)



@app.route('/')
def show_phrase():
    histogram = list_of_lists_histogram('aristotlePoetry.txt')
    sentence = get_sentence(histogram)
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')