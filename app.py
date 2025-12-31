<<<<<<< HEAD
from flask import (Flask, jsonify)
import os

app = Flask(__name__)

@app.route('/')

def hello():
    # It looks for CUSTOM_MESSAGE; if it's not found, it uses a default
    msg = os.getenv("CUSTOM_MESSAGE", "Default Hello")
    color = os.getenv("APP_COLOR", "white")
    return {
        "message": msg,
        "color_setting": color,
        "status": "success",
        "version": "2.0.0"
    }

if __name__ == '__main__':
=======
from flask import (Flask, jsonify)
import os

app = Flask(__name__)

@app.route('/')

def hello():
    # It looks for CUSTOM_MESSAGE; if it's not found, it uses a default
    msg = os.getenv("CUSTOM_MESSAGE", "Default Hello")
    color = os.getenv("APP_COLOR", "white")
    return {
        "message": msg,
        "color_setting": color,
        "status": "success",
        "version": "2.0.0"
    }

if __name__ == '__main__':
>>>>>>> 5cacd72 (first commit)
    app.run(host='0.0.0.0', port=5000)