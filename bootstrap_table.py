from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User3(db.Model):
    date1 = db.Column(db.String(64), primary_key=True)
    vikram = db.Column(db.Integer, index=True)
    neeraj = db.Column(db.Integer, index=True)
    link = db.Column(db.String(256))
    headline = db.Column(db.String(256))

db.create_all()


@app.route('/')
def index():
    users = User3.query
    return render_template('bootstrap_table.html', title='Bicycle Table',
                           users=users)


if __name__ == '__main__':
    app.run()
