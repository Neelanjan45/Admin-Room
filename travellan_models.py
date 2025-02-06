from app import db

class Locations(db.Model):
    __bind_key__ = 'travellan'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(600), index=False, unique=False)

    sites = db.relationship('Sites', backref='location', lazy='dynamic', cascade="all, delete")

    def __repr__(self):
        return self.title

class Sites(db.Model):
    __bind_key__ = 'travellan'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(600), index=False, unique=False)
    image = db.Column(db.String(200), index=False, unique=False)
    loc_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
