from flask import Flask
from main import rec

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Returning the Recamán's sequence!</p>"

@app.route('/num/<int:cnt>')
def get_rec(cnt):
    print(cnt)
    rec_gen = rec()
    res = [next(rec_gen) for _ in range(cnt)]
    return str(res)

if __name__ == '__main__':
    app.run()