from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return 'o otavio é gay'

@app.get('/teste/<userName>')
def user(userName):
    return f"ola {userName}"

if __name__ == '__main__':
    app.run()