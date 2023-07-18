
# A web app which. See LinkedIN video from Ronnie Sheer.


from distutils.log import debug
# Flask get you quickly get things on the web. Below I have a web application code.
from flask import Flask
# Instantiate (represent) a flask object
app = Flask(__name__)

# Decorator (to turn into routes the below def)
@app.route("/")

def hello():
    
    return "Hello, World!"

app.run(debug = True)



