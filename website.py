from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('这是一个用python搭建的网站')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)