from flask import Flask, request
from socket import gethostname
from subprocess import Popen

app = Flask(__name__)

@app.route('/', methods=['POST'])
def increment():
    global x
    Popen("python3 $(pwd)/stress_cpu.py", shell=True)
    return "{}"

@app.route('/', methods=['GET'])
def get():
    return str(gethostname())

app.run(host='0.0.0.0')