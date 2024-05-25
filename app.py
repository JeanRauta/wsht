from flask import Flask , render_template
import demucs.api


app = Flask(__name__)

@app.route('/')
def index():
    teste = 'jean bonito'
    return render_template('index.html', texto=teste)

@app.get('/teste/<userName>')
def user(userName):
    return f"ola {userName}"

if __name__ == '__main__':
    app.run()

