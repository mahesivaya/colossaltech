from flask import Flask

app = Flask(__name__)

@app.route('/flask')
def hello():
    return 'Hello'


if __name__=='__main__':
    app.run(debug=True)