from flask import render_template, url_for
from app import app


@app.route('/')
def home():  # put application's code here

    return render_template('homePage.html', title='Home')

