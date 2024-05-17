from flask import Flask , render_template
from chord_extractor.extractors import Chordino

app = Flask(__name__)

@app.route('/')
def index():
    chordino = Chordino()
    acordes = chordino.extract(caminho_da_musica)
    caminho_da_musica = "./static/teste.wav"
    for acorde in acordes:
        print(acorde.chord)

    return render_template('index.html')

@app.get('/teste/<userName>')
def user(userName):
    return f"ola {userName}"

if __name__ == '__main__':
    app.run()

