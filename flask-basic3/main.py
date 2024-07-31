from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  # return "hello"
  return "<h1 style='color: red;'>hello</h1>"\
  "<p>paragraph</p>"\
  "<img src='http://picsum.photos/400?random=1' />"

# @app.route("/test")
# def test():
#   return "test"


@app.route("/test/<id>")
def test(id):
  return f"id:{id}番です。"


# デバックモード
# flask --app hello --debug run
