from flask import Flask, render_template, redirect, url_for, request
import pickle
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import model_from_json
from keras import backend as K


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    K.clear_session()
    category = None
    return render_template('home.html', category=category)


if __name__ == '__main__':
    app.run(debug = True)
