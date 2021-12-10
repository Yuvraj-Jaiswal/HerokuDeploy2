from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello heroku</h1>"


if __name__ == '__main__':
    # web.debug = True
    app.run()
