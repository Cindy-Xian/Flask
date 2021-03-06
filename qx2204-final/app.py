# *******************************************************
# Name: Qi Xian
# UNI: qx2204
# Create a personal website
# *******************************************************

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    '''
    create a home page
    '''
    return render_template("index.html")


@app.route("/assignments")
def assignments():
    '''
    create a assignments page
    '''
    return render_template("assignments.html")

@app.route("/classes")
def classes():
    '''
    create a classes page
    '''
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()