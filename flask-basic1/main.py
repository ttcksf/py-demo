from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "hello"

# pip install Flask 
# flask --app main run 
# https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/quickstart.html
