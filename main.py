from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/novellas")
def novellas():
    return render_template("novellas.html")

@app.route("/music")
def music():
    return render_template("music.html")

if __name__ == "__main__":
    app.run(debug=True)
