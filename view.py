from flask import Flask, render_template, request
from model import Person
import controller 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('vista-1.html')

@app.route('/add_person', methods=['POST'])
def add_person():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['Last_name']
        id = request.form['id']
        controller.add_person(id, first_name, last_name)
        return 'recibido!'



