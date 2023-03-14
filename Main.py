from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    time = datetime.datetime.now()
    return render_template("index.html", dt=time)

@app.route('/mappa/<width>/<height>', methods=['GET'])
def size_1(width, height):
  time = datetime.datetime.now()
  return render_template("index1.html", dt=time, width=width, height=height)




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)