from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'lalalala survery lala'

@app.route()
def form():
    return render_template('survey.html')

if __name__ == "__main__":
    app.run(debug = True)