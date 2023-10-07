from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# iniciar o flask
app = Flask(__name__)

@app.route('/inicio')

def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista_de_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html',titulo = 'Jogos', jogos = lista_de_jogos)


@app.route('/novo')

def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')


app.run(host='0.0.0.0', port=8080)