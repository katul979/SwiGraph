from swigraph import db

class Nodes(db.Model):
    """Nodes table storing lat, long of all the nodes"""
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

class Connections(db.Model):
    """Connection table storing connection between two nodes as well as peak hours time info"""
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer)
    connected_to = db.Column(db.Integer)
    time_peak_one = db.Column(db.Integer)
    time_peak_two = db.Column(db.Integer)
    time_peak_three = db.Column(db.Integer)
