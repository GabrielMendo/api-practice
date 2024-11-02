from flask import Flask , render_template

app = Flask(__name__)

@app.route("/<name>/<day>")
def hello_world(name,day):
        return "Hello" + name + "today is " + day


@app.route("/<number>")
def check_number(number):
  if int(number) > 10:
    return "Greater than 10"
  elif int(number) < 10:
    return "Less than 10"
  else:
    return "Equal to 10"


# @app.route("/api/<key>")
# def api(key)
    


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')