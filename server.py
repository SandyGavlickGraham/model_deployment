from flask import Flask
import random
from flask import render_template
from flask import request
from model import predict

# Create the flask application.
#  We can then use the 
# application to define routes,
#  or urls within our webserver.
app = Flask(__name__)

# The @ prefix defines a python
# decorator that will act on the
# function definition that 
# follows it.
# 
# What we are saying here is 
# that when the / url is 
# visited, run the index 
# function, and whatever the 
# function returns will be what
# the web server returns to the
# browser.
# @app.route('/')
# def the_home_page():
#     print('You have a visitor!')
#     return 'Hello, World!'
@app.route('/')
def index():
    return render_template('index.html', name='Ada')

@app.route('/ada')
def ada_page():
    return 'The ada cohort is my favorite data science cohort!'


@app.route('/roll-dice')
def roll_dice():
    return render_template('roll-dice.html', number=str(random.randint(1,6)))

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')


@app.route('/make-greeting')
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting.html', greeting=greeting)

# Create the form outlined in the lesson above.

# Displaying Model Output

# Create a form that contains inputs that map to your model's inputs
# Write an endpoint that feeds that input into a trained model
# Display the model's prediction in html

@app.route('/model-form')
def my_model_form():
    return render_template('model-form.html')


@app.route('/model',methods=['POST'])
def handle_model_form_submission():
    message = request.form['message']
    answer = predict(message)
    return render_template('model.html', message=message, answer=answer)


@app.route('/bootstrap-demo')
def bootstrap_demo():
    return render_template('bootstrap.html')