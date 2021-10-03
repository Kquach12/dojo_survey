from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja


@app.route('/')
def form():
    return render_template('survey.html')

# @app.route('/collect')
# def collect():
#     data = {
#         "name": request.form['name'],
#         "location": request.form['location']
#         "languages": request.form['language']
#         "comments": request.form['comments']
#     }
#     Ninja.save(data)

@app.route('/collect', methods = ['POST'])
def collect():
    if not Ninja.validate_ninja(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comments": request.form['comments']
    }
    Ninja.save(data)

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')