from flask import request, jsonify
import json
from swigraph import app, db
from .models import Nodes
from .methods import get_nearest_node, ucs

@app.route("/")
def hello():
    return "Welcome to SwiGraph!"

@app.route("/nodes", methods=['GET'])
def get_nodes():
    nodes = []
    offset = int(request.args.get('offset', '0'))
    limit = int(request.args.get('limit', '50'))
    for n in db.session.query(Nodes)\
                    .offset(offset).\
                       limit(limit):
        node = {
            'id': n.id,
            'lat': n.lat,
            'lon': n.lon
        }
        nodes.append(node)
    return jsonify(nodes=nodes)

@app.route("/path", methods=['GET'])
def get_path():
    error = None
    status_code = 200
    path = []
    start_lat = float(request.args.get('start_lat', '0'))
    start_lon = float(request.args.get('start_lon', '0'))
    end_lat = float(request.args.get('end_lat', '0'))
    end_lon = float(request.args.get('end_lon', '0'))
    option = int(request.args.get('option', '0'))
    peak = int(request.args.get('peak', '1'))
    if start_lat != 0 and start_lon != 0 and end_lat != 0 and end_lon != 0:
        start = get_nearest_node(start_lat, start_lon)
        goal = get_nearest_node(end_lat, end_lon)
        if start is not None and goal is not None:
            path = ucs(start, goal, option, peak)
        else:
            error = "No Path Exists!"
            status_code = 400
    else:
        error = "Bad Request!"
        status_code = 400
    if error is None:
        return jsonify(path=path)
    else:
        response = jsonify(error=error)
        response.status_code = status_code
        return response
