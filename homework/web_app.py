## web_app.py
"""Web application to deploy the model"""

from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"

@app.route("/index")
def index():
    
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
    