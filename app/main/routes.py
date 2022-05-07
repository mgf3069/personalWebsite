from flask import render_template, url_for, redirect
from app import app


@app.route('/')
def home():  # put application's code here
    return render_template('homePage.html', title='Home')


@app.route('/projects')
def project_page():
    return render_template('projects.html', title='Projects')


@app.route('/contact')
def contact_page():
    return render_template('contact.html', title='Contact')


@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html', title='Gallery')


@app.route('/linkedIn')
def linkedin_page():
    return redirect('https://www.linkedin.com/in/michael-fields-552845236/')
