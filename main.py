import sys
import traceback
from flask import Flask

app = Flask(__name__)

try:
    import requests
    print("requests imported successfully")
except Exception as e:
    with open("/tmp/error.log", "w") as f:
        traceback.print_exc(file=f)
    print("Import Error occurred. Check /tmp/error.log")

@app.route('/')
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
