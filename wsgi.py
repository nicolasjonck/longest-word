from flask import Flask, render_template, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    game = Game()
    if not session: session["score"] = 0
    return render_template('home.html', grid=game.grid, score=0)


@app.route('/check', methods=["POST"])
def check():
    print(session)
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)

    if is_valid:
        session["score"] = session["score"] + 1

    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
