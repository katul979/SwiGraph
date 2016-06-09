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

class Durations(db.Model):
    """Duration to travel connection at a given time bucket"""
    id = db.Column(db.Integer, primary_key=True)
    interval = db.Column(db.Integer)
    time_req = db.Column(db.Integer)
    connection_id = db.Column(db.Integer, db.ForeignKey('connections.id'))
