from flask import Flask

app=Flask("__name__")

@app.route("/")
def index():
    return "HEllo,World"
@app.route("/<string:name>")
def arshad(name):
    name=name.capitalize()
    return f"HELLO FEARMAN {name}"