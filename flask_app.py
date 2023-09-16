from bardapi import Bard
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash, g
from keys import bard_key
import os
import time

# initialize Flask app
app = Flask(__name__)
os.environ['_BARD_API_KEY'] = bard_key

#homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        print(input_text)
        answer = Bard().get_answer(input_text)['content']
        print(answer)
        return render_template('index.html', answer=answer)
    else:
        return render_template('index.html')
    



'''
input_text = "What is APCSP"

print(Bard().get_answer(input_text)['content'])

'''