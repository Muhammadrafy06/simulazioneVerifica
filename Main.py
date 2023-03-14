from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    time = datetime.datetime.now()
    return render_template("index.html", dt=time)
@app.route('/700', methods=['GET'])
def size_1():
  return render_template("index1.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)