from server import app, config
from flask import Flask, render_template
from flask import request
from flask import jsonify
from random import randint
from controller import as_points, valid_points, area, as_num, is_isosceles

@app.route('/')

def base():
    return render_template("template.html")

@app.route('/square', methods=['GET'])
def calculate_square():
    arg_area = as_num(request.args.get('area', None))
    points = request.args.get('points', None)
    points = as_points(request.args.get('points', None), app.logger)
    if arg_area and points and len(points) == 4:
        if valid_points(points, 'square') and area(points, 'square', app.logger) == arg_area:
            return 'response = true;', 200
    return 'response = false;', 200

@app.route('/triangle', methods=['GET'])
def calculate_triangle():
    arg_area = as_num(request.args.get('area', None))
    shape = request.args.get('type', None)
    points = request.args.get('points', None)
    points = as_points(request.args.get('points', None), app.logger)
    if arg_area and points and len(points) == 3:
        if valid_points(points, 'triangle') and area(points, 'triangle', app.logger) == arg_area:
            if (shape == 'isosceles' and is_isosceles(points, app.logger)) or shape == 'other' and not is_isosceles(points, app.logger):
                return 'response = true;', 200
    return 'response = false;', 200
