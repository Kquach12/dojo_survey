from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'lalalala survery lala'

@app.route('/')
def form():
    return render_template('survey.html')


@app.route('/collect', methods = ['POST'])
def collect():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug = True)