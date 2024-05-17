from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/teste/<userName>')
def user(userName):
    return f"ola {userName}"

if __name__ == '__main__':
    app.run()