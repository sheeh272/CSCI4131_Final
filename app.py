from flask import Flask, request, Response, render_template, flash, json, redirect, url_for
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextField
from wtforms.validators import Regexp
import re
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import os

class WordForm(FlaskForm):
    player = SelectField("player", choices = [("Anatoly Karpov","Anatoly Karpov"),("Garry Kasparov","Garry Kasparov"),("José Raúl Capablanca","José Raúl Capablanca")])
    selection = SelectField("selection", choices = [("1","exercises"),("2","games"),("3","playerInfo")])
    submit = SubmitField("Go")

class LoginForm(FlaskForm):
    Username = StringField("Username",  validators=[DataRequired()])
    Passcode = StringField("Passcode",  validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    Username = StringField("Username",  validators=[DataRequired()])
    Passcode = StringField("Passcode",  validators=[DataRequired()])
    submit = SubmitField("register")

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)
bootstrap = Bootstrap(app)


    
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
#db.session.execute('DROP TABLE games')
#db.session.execute('DROP TABLE users')
#db.session.execute('DROP TABLE players')
#db.session.execute('DROP TABLE tactics')


db.session.execute('CREATE TABLE IF NOT EXISTS games(player1 TEXT, player2 TEXT, notation TEXT);')
db.session.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, passcode Text);')
db.session.execute('CREATE TABLE IF NOT EXISTS players(name TEXT,flag TEXT);')
db.session.execute('CREATE TABLE IF NOT EXISTS tactics(name TEXT,puzzleImg TEXT,solution TEXT);')

db.session.execute('DROP TABLE games')
#db.session.execute('DROP TABLE users')
db.session.execute('DROP TABLE players')
db.session.execute('DROP TABLE tactics')

#
db.session.execute('CREATE TABLE IF NOT EXISTS games(player1 TEXT, player2 TEXT, notation TEXT);')
db.session.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, passcode Text);')
db.session.execute('CREATE TABLE IF NOT EXISTS players(name TEXT,flag TEXT);')
db.session.execute('CREATE TABLE IF NOT EXISTS tactics(name TEXT,puzzleImg TEXT,solution TEXT);')

db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Anatoly Karpov','Veslin Topalov',:notation)",{'notation': open("./static/games/Karpov-Topalov.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Garry Kasparov','Viswanathan Anand',:notation)",{'notation': open("./static/games/Kasparov-Anand.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Vladimir Kramnik','Garry Kasparov',:notation)",{'notation': open("./static/games/Kramnik-Kasparov.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Michael Adams','Garry Kasparov',:notation)",{'notation': open("./static/games/Adams-Kasparov.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Anatoly Karpov','Viktor Korchnoi',:notation)",{'notation': open("./static/games/Karpov-Korchnoi.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Anatoly Karpov','Boris Spassky',:notation)",{'notation': open("./static/games/Karpov-Spassky.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('José Raúl Capablanca','Frank James Marshall',:notation)",{'notation': open("./static/games/Capablanca-Marshall.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('Ossip Bernstein','José Raúl Capablanca',:notation)",{'notation': open("./static/games/Bernstein-Capablanca.txt","r").read().replace('\n', '')})
db.session.execute("INSERT INTO games (player1,player2,notation) VALUES('José Raúl Capablanca','Marc Fonaroff',:notation)",{'notation': open("./static/games/Capablanca-Fonaroff.txt","r").read().replace('\n', '')})

db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic1A.png','Rxg2 Kf1 Bc4+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic2A.png','Nxe4')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic3A.png','a6 Be2 Bd7')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic4A.png','Rxh7')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic5A.png','Re7')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic6A.png','Bh7+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic7A.png','Rxc4')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic8A.png','h6')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic9A.png','Bxd4 Nxd4 Ne5 Qxf4 Nxd3')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('José Raúl Capablanca','/static/tactics/tactic10A.png','Rxc3 Rxc3 Qb2')")

db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic1B.png',' Qxa3 w/Rxb8+ Rc1 & R1c8  ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic2B.png','...Bxf2+ (if ...Nxe4 Ng6#)')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic3B.png',' Rxd6+ w/Qxd8+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic4B.png',' Qa3 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic5B.png','g3+ Kh3 Nf2+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic6B.png','Rc1 w/Nb5 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic7B.png',' Nxf3 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic8B.png','Nxd4 w/Bf4')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic9B.png','Rg7')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Anatoly Karpov','/static/tactics/tactic10B.png","Ba6 ')")

db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic1C.png',' Rxc8 Nxc8 Rxc8 Qxc8 Qa3+ ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic2C.png',' Rxf7 Rxf7 Rxf7 if Rh8 h4')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic3C.png',' Qg4 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic4C.png',' Bxg6 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic5C.png','Qc1+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic6C.png","Nxe6 if Qb6 Nc7+ ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic7C.png',' Rc5 if Nb7 Rc8+ ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic8C.png','Bxf5 ')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic9C.png',' ...Rxb2 if Qxb2 Bxd4+')")
db.session.execute("INSERT INTO tactics (name,puzzleImg,solution) VALUES('Garry Kasparov','/static/tactics/tactic10C.png','...Na5 ')")

db.session.execute("INSERT INTO players (name,flag) VALUES('Garry Kasparov','/static/flags/RussianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Viswanathan Anand','/static/flags/IndianFlag.jpg')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Vladimir Kramnik','/static/flags/RussianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Michael Adams','/static/flags/EnglishFlag.jpg')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Veslin Topalov','/static/flags/BulgarianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Anatoly Karpov','/static/flags/RussianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Viktor Korchnoi','/static/flags/RussianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Boris Spassky','/static/flags/RussianFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('José Raúl Capablanca','/static/flags/CubanFlag.jpg')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Frank James Marshall','/static/flags/USFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Ossip Bernstein','/static/flags/FrenchFlag.png')")
db.session.execute("INSERT INTO players (name,flag) VALUES('Marc Fonaroff','/static/flags/USFlag.png')")
db.session.commit()


#res = db.session.execute('SELECT * FROM games')
#print(res.fetchall())
@app.route('/about',methods=['GET', 'POST'])
@csrf.exempt
def about():
      return render_template("about.html")

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db.session.execute('INSERT INTO users (username,passcode) Values(:user,:passcode)',
        {'user':form.Username.data,'passcode':form.Passcode.data})
        db.session.commit()
        flash("user registered")
    return render_template("register.html", form = form)

@app.route('/login',methods=['GET', 'POST'])
@csrf.exempt
def login():
    form = LoginForm()
    if form.validate_on_submit():
        passcode = db.session.execute('SELECT passcode FROM users WHERE username = :val',{'val':form.Username.data})
        row = passcode.fetchone()
        if row == None:
            flash("wrong username")
            return render_template("login.html", form = form)
        passcode = row['passcode']
        
        if passcode == form.Passcode.data:
            return redirect(url_for('index'))
        else:
            flash("wrong passcode")
            return render_template("login.html", form = form)
    else:
         print("error")
    return render_template("login.html", form = form)

@app.route('/index', methods=['POST','GET'])
@csrf.exempt
def index():
    form = WordForm()
    return render_template("index.html", form=form)


#@app.route('/index')
#def index():
@app.route('/playerInfo', methods=['POST','GET'])
@csrf.exempt
def playerInfo():
    form = WordForm()
    if form.validate_on_submit():
        player = form.player.data
        selection = int(form.selection.data)
    else:
        alert("error")
       #return render_template("index.html", form=form)
    if selection == 3:
        return render_template("playerInfo.html", playerName = player, playerNamejson = json.dumps(player))
    elif selection == 2:
        #moves = db.session.execute('SELECT notation FROM GAMES WHERE player1 = :val OR player2 = :val',{'val': player})
        moves = db.session.execute('SELECT * FROM GAMES WHERE player1 = :val OR player2 = :val',{'val': player})
        gameList = []
        flagListP1 = []
        flagListP2 = []
        for x in moves:
            gameList.append(x['notation'])
            flag1 = db.session.execute('SELECT flag FROM players WHERE name = :val',{'val':x['player1']})
            flagListP1.append((x['player1'],flag1.fetchone()['flag']))
            flag2 = db.session.execute('SELECT flag FROM players WHERE name = :val',{'val':x['player2']})
            flagListP2.append((x['player2'],flag2.fetchone()['flag']))
        #print(test)
        return render_template("chessGames.html",notation = json.dumps(gameList),player1Info= flagListP1, player2Info = flagListP2,
        player1Infojson = json.dumps(flagListP1),player2Infojson = json.dumps(flagListP2))
        #return redirect(url_for('login'))
    elif selection == 1:
        query = db.session.execute('SELECT * FROM tactics WHERE name = :val',{'val':player})
        imgs = []
        solutions = []
        for x in query:
            imgs.append(x['puzzleImg'])
            solutions.append(x['solution'])
        return render_template("tactics.html", tacticImg = imgs, tacticSol = solutions, player = player,
        tacticImgjson = json.dumps(imgs), tacticSoljson = json.dumps(solutions))


    return render_template("index.html", form=form)
    #return render_template("playerInfo.html", playerName = "Bobby Fisher")

#@app.route('/playerInfo', methods=['POST','GET'])
#def playerInfo():
#     return render_template("playerInfo.html", playerName = "Bobby Fisher")


@app.route('/proxy')
def proxy():
    result = requests.get(request.args['url'])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp


