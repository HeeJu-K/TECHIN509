from flask import Flask, render_template, request
from logic import *

app = Flask(__name__)

#initialize 
game_board = Game(Human('X'), Human('O'))
username1 = "P1"
username2 = "P2"
game_mode = "PVP"
count = 0
bot = Bot('O')


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    return render_template('start.html', error=error)

@app.route('/newgame', methods=['POST'])
def modeselect():
    global game_board
    global game_mode
    global username1
    global username2
    global count
    global bot
    username1 = request.form.get('username1')
    player_num = request.form.get('player', type=str)
    if player_num == 'single player':
        game_mode="PVE"
        username2 = "Bot"
        game_board = Game(Human('X'), bot)
    elif player_num == 'multi player':
        game_mode="PVP"
        username2 = request.form.get('username2')
        game_board = Game(Human('X'), Human('O'))
    return render_template('play.html', board=game_board.board.getBoard(), symbol=game_board.get_cur_player(), game_mode=game_mode)


@app.route("/play/<int:x>/<int:y>")
def play(x, y):
    symbol = game_board.get_cur_player()
    if game_mode == "PVE":
        game_board.board.set(x, y, symbol)
        winner = game_board.run()
        if winner != None:
                return render_template('winner.html', winner=winner, username1=username1, username2=username2, game_mode=game_mode)
        bot.get_move( game_board.board)
        game_board.get_next_player()
    elif game_mode == "PVP":
        game_board.board.set(x, y, symbol)

    winner = game_board.run()
    if winner != None:
        return render_template('winner.html', winner=winner, username1=username1, username2=username2, game_mode=game_mode)
    elif game_board.board.count == 8:
        return render_template('winner.html', winner=winner, username1=username1, username2=username2, game_mode=game_mode)
    else:
        return render_template('play.html', board=game_board.board.getBoard(), symbol=game_board.get_next_player(), username1=username1, username2=username2, game_mode=game_mode)
