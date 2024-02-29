
# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# import random


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# class Gamerecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     player_choice = db.Column(db.String, nullable=False)
#     computer_choice = db.Column(db.String, nullable=False)
#     result = db.Column(db.String, nullable=False)


# RSP = ['가위', '바위', '보']


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/play', methods=['POST'])
# def play():
#     player_choice = request.form['choice']
#     computer_choice = random.choice(RSP)

#     result = determine_winner(player_choice, computer_choice)

#     with app.app_context():
#         record = Gamerecord(player_choice=player_choice, computer_choice=computer_choice, result=result)
#         db.session.add(record)
#         db.session.commit()

#     return redirect(url_for('result'))


# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return 'Draw'
#     elif (player_choice == '가위' and computer_choice == '보') or (player_choice == '바위' and computer_choice == '가위') or (player_choice == '보' and computer_choice == '바위'):
#         return 'Win'
#     else:
#         return 'lose'


# @app.route('/result')
# def result():
#     game_records = Gamerecord.query.all()
#     return render_template('result.html', game_records=game_records)


# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)


#  오류

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class GameRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)


RSP = ['가위', '바위', '보']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = random.choice(RSP)

    result = determine_winner(player_choice, computer_choice)

    record = GameRecord(player_choice=player_choice,
                        computer_choice=computer_choice, result=result)
    db.session.add(record)
    db.session.commit()

    return redirect(url_for('result'))


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return '무승부'
    elif (player_choice == '가위' and computer_choice == '보') or \
         (player_choice == '바위' and computer_choice == '가위') or \
         (player_choice == '보' and computer_choice == '바위'):
        return '이겼습니다!'
    else:
        return '졌습니다!'


@app.route('/result')
def result():
    game_records = GameRecord.query.all()
    return render_template('result.html', game_records=game_records)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
