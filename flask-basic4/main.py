from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  # return "hello"
  # templatesフォルダの中を探しにいく仕組み
  return render_template("index.html")



# デバックモード
# flask --app hello --debug run
