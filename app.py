from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# the values assaigned to the database are entered
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:derand@localhost:3306/todoDB'
# I am using a form so I need a secretkey
# it was randomly typed in
app.config['SECRET_KEY'] = 'wyugfu'

db = SQLAlchemy(app)

# simple database


class Todo(db.Model):
    # has the is as primary key
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # the text of teh task can be a max of 75 chars long
    text = db.Column(db.String(75), nullable=False)
    # is the task completed??
    complete = db.Column(db.Boolean, nullable=False)


@app.route('/')
def index():
    # this is the home page
    # separated if the task is true
    incomplete = Todo.query.filter_by(complete=False).all()
    # separated and if the task is completed
    complete = Todo.query.filter_by(complete=True).all()
    # the data is returned and can be used in the html
    return render_template('indexx.html', incomplete=incomplete, complete=complete)

# its a form so requires a post request


@app.route('/new tasks', methods=['POST'])
def add():
    # you can add new features to this
    todo = Todo(text=request.form['todolist'], complete=False)
    # adds a new value to the db
    db.session.add(todo)
    # saves it
    db.session.commit()
    # returns/refreshes the page
    return redirect(url_for('indexx'))


@app.route('/completed tasks/<id>')
def complete(id):
    # check by id
    todo = Todo.query.filter_by(id=int(id)).first()
    # if its completed the value is chnaged
    todo.complete = True
    # chnge is saved to db
    db.session.commit()
    # refreshes/returns the page
    return redirect(url_for('indexx'))


# run the app with debug true
# on the localhost and at port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
