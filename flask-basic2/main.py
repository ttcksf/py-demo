from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "hello"

# @app.route("/test")
# def test():
#   return "test"


@app.route("/test/<id>")
def test(id):
  return f"id:{id}番です。"

# pip install Flask 
# flask --app main run 
# https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/quickstart.html
# デバックモード
# flask --app hello --debug run
