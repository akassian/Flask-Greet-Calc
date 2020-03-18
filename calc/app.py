# Put your app in here.
from flask import Flask, request

import operations

app = Flask(__name__)


@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.add(a, b))


@app.route("/sub")
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.sub(a, b))


@app.route("/mult")
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.mult(a, b))


@app.route("/div")
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.div(a, b))


@app.route("/math/<calc_op>")
def calc_operation(calc_op):
    CALC_OPS = {
        'add': add(),
        'sub': sub(),
        'mult': mult(),
        'div': div()
    }
    return CALC_OPS[calc_op]
