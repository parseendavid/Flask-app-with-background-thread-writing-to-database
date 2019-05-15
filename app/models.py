from app import db

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String(80), nullable=False)
    setup = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Joke %r>' % self.id
