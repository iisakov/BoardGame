#!venv/bin/python
from flask import Flask, render_template, request, redirect
from datetime import datetime, date, timedelta
import secrets, hashlib
import os

from Tools.Maker import Maker

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Добро пожаловать')


@app.route("/board_game/gallery/")
@app.route("/board_game/", methods=['GET'])
def gallery():
    param = request.args.to_dict()
    if 'num_players' in param and 'num_gex' in param:
        Maker.make_request_game(num_players=int(param['num_players']), num_gex_in_hand=int(param['num_gex']))
    data = {'next_day': date.today() + timedelta(1),
            'previous_day': date.today() - timedelta(1),
            'now': date.today()}
    return render_template('board_game/gallery_main.html', title='GEXOPOLICE', data=data)


@app.route("/board_game/gallery/<day>")
def gallery_for_day(day):
    true_date = datetime.strptime(day, "%Y-%m-%d").date()
    data = {'next_day': true_date + timedelta(1),
            'previous_day': true_date - timedelta(1),
            'true_day': true_date,
            'now': date.today()}

    items = os.listdir(f'./static/board_game/{true_date}/img/') if os.path.isdir(f'./static/board_game/{true_date}/img/') else 0
    return render_template('board_game/gallery_day.html', title='GEXOPOLICE - Gallery', day=day, data=data, items=sorted(items) if type(items) == list else 0)


@app.route("/board_game/gallery/<day>/<game>")
def gallery_for_game(day, game):
    true_date = datetime.strptime(day, "%Y-%m-%d").date()
    data = {'next_day': true_date + timedelta(1),
            'previous_day': true_date - timedelta(1),
            'true_day': true_date,
            'now': date.today()}
    return render_template('board_game/gallery_game.html', title='GEXOPOLICE - Game', day=day, data=data, game=game)


@app.route("/board_game/gallery/autogenerate_game/<day>")
def gallery_autogenerate_game(day):
    Maker.make_standard_game(100, 1, day=day)
    return redirect(f'/board_game/gallery/{day}')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
