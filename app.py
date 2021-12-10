from flask import Flask,render_template,request

web = Flask(__name__)

@web.route('/', methods=['GET'])
def index():
    return "<h1>Hello heroku</h1>"


if __name__ == '__main__':
    # web.debug = True
    web.run()
