from datetime import datetime

from blog import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    content = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_on': self.created_on
        }

    def __repr__(self):
        return '<Post {}>'.format(self.title)
