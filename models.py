from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)
    done = db.Column(db.Boolean, default=False) #with "default=False" the default value of done will be false. I can use that for no required fields.
    username = db.Column(db.String(50), nullable=False) #with "nullable=False" if this element is empty or not, doesn't matter.

    '''for view the contacts whit a define format'''
    def __repr__(self):
        return '<Todo %r>' % self.label    
    
    '''for view the contacts whit a define format'''
    def serialize(self):
        return{
            'id':self.id,
            'label':self.label,
            'done':self.done,
            'username': self.username
        }           