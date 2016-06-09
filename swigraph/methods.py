from swigraph import app, db
import heapq
from math import sin, cos, sqrt, atan2, radians
from .models import Nodes, Connections, Durations

def get_distance(lat_1, long_1, lat_2, long_2):
    """Simply get distance between two points defined by (latitude, longitude)"""
    R = 6373.0
    lat1 = radians(lat_1)
    lon1 = radians(long_1)
    lat2 = radians(lat_2)
    lon2 = radians(long_2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def get_nearest_node(lat, lon):
    """Returns the nearest node from the database, this return is dummy"""
    return Nodes.query.get(1)

def ucs(start, goal, option, interval):
    """Uniform Cost Search to get shorted path between two nodes depending on the cost"""
    q = [(0, node, [])]
    explored = {}
    while q:
        cost, point, path = heapq.heappop(q)
        if explored.has_key(point) and explored[point] < cost:
            continue
        path = path + [point]
        if point == goal:
            return path
        for n in get_neighbours(point):
            if n not in explored:
                n_cost = get_cost(point, n, option, interval)
                heapq.heappush(q, (cost + n_cost, n, path))
        explored[point] = cost
    return None

def get_neighbours(point):
    """Get all neighbours of a node"""
    return Connections.query.filter_by(node_id=point.id).all()

def get_cost(point, n, option, interval):
    """Get cost (distance or time) of travelling from one node to other,
    'point' and 'n' will always be adjacent here"""
    cost = 0
    if option == 0:
        cost = get_distance(point.lat, point.lon, n.lat, n.lon)
    else:
        connection = Connections.query.filter_by(node_id=point.id).filter_by(connected_to=n.id).first()
        duration = Durations.query.filter_by(connection_id=connection.id).filter_by(interval=interval).first()
        cost = duration.time_req
    return cost
