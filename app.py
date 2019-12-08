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
    if request.method == 'POST':
        if request.form['question']:

                json_file = open('DEEP_MODEL.json', 'r')
                loaded_model_json = json_file.read()
                json_file.close()
                loaded_model = model_from_json(loaded_model_json)
                loaded_model.load_weights("DEEP_MODEL.h5")
                with open('tokenizer.pickle', 'rb') as file:
                    tokenizes= pickle.load(file)
                file.close()

                ques = str(request.form['question'])
                ques = [ques]
                seq = tokenizes.texts_to_sequences(ques)
                padded = pad_sequences(seq, maxlen=200)
                pred = loaded_model.predict(padded)
                labels= ['unknown', 'what', 'when', 'who', 'affirmation']
                category = labels[np.argmax(pred)]

        else:
            category = "type something"
    return render_template('home.html', category=category)


if __name__ == '__main__':
    app.run(debug = True)
