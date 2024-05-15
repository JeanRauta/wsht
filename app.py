from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return 'app renderizado'

@app.get('/teste/<userName>')
def user(userName):
    return f"ola {userName}"

if __name__ == '__main__':
    app.run()