from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    time = datetime.datetime.now()
    return render_template("index.html", dt=time)

@app.route('/600', methods=['GET'])
def size_1():
  time = datetime.datetime.now()
  return render_template("index1.html", dt=time)

@app.route('/800', methods=['GET'])
def size_2():
  time = datetime.datetime.now()
  return render_template("index2.html", dt=time)

@app.route('/1000', methods=['GET'])
def size_3():
  time = datetime.datetime.now()
  return render_template("index3.html", dt=time)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)