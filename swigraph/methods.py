from swigraph import app, db
import heapq
from math import sin, cos, sqrt, atan2, radians
from .models import Nodes, Connections

def get_distance(lat_1, long_1, lat_2, long_2):
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
    """Returns the nearest node from the database"""
    return Nodes.query.get(1)

def ucs(start, goal, option, peak):
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
                n_cost = get_cost(point, n, option, peak)
                heapq.heappush(q, (cost + n_cost, n, path))
        explored[point] = cost
    return None

def get_neighbours(point):
    return Connections.query.filter_by(node_id=point.id).all()

def get_cost(point, n, option):
    cost = 0
    if option == 0:
        cost = get_distance(point.lat, point.lon, n.lat, n.lon)
    else:
        connection = Connections.query.filter_by(node_id=point.id).filter_by(connected_to=n.id).first()
        if peak == 1:
            cost = connection.time_peak_one
        elif peak == 2:
            cost = connection.time_peak_two
        else:
            cost = connection.time_peak_three
    return cost
