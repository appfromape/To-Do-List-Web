from flask import Flask, render_template, url_for, request, jsonify, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    
# db.create_all()

@app.route('/')
def get_all_posts():
    posts = Todo.query.all()
    return render_template("index.html", all_posts=posts)

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        print(request.form.get('item'))
        new_item = Todo(
            content = request.form['item']
        )
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == 'POST':
        a = request.form['keyword']
        print(a)
        todo = Todo.query.filter_by(content=a).first()
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("get_all_posts"))

if __name__ == "__main__":
    app.run(debug=True)