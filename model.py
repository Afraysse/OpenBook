"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User information."""

    __tablename__ = "user"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)


    # draft_count = db.Column(db.Integer, nullable = True)
    # publish_count = db.Column(db.Integer, nullable = True)

    def __repr__(self):

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)

    
class Book(db.Model):
    """Stores drafts being written by user."""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    draft = db.Column(db.String(10000), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime)

    # Define relationship to User
    user = db.relationship("User", backref=db.backref("books", order_by=user_id))


    def __repr__(self):

        return "<Book book_id=%s draft=%s title=%s>" % (self.book_id, self.draft, self.title)



class Published(db.Model):
    """Stores published drafts written by user."""

    __tablename__ = "published"

    publish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime)

    # # Define relationship to User
    user = db.relationship("User", backref=db.backref("published"))

    # Define relationship to Books 
    book = db.relationship("Book", backref=db.backref("published", order_by=date))

    def __repr__(self):

        return "<Published publish_id=%s title=%s user_id=% book__date=%>" % (self.publish_id, 
                                                                            self.title, 
                                                                            self.user_id, 
                                                                            self.book_date)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///openbook'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
