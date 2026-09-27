from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is Running!"

@app.route("/startup")
def startup():
    return "Startup OK"

@app.route("/ready")
def ready():
    return "Ready OK"

@app.route("/live")
def live():
    return "Live OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)