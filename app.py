from flask import Flask, render_template,request,redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Todo.db"
app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False


db = SQLAlchemy(app)
class tododb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
         
    def __repr__(self):
        return f"task is : {self.task} and desc is : {self.desc}"   


@app.route("/", methods = ["GET" ,"POST"])
def create():
    if request.method == "POST":
        Title = request.form.get("title")
        Desc = request.form.get("desc")
        new_task = tododb(task=Title, desc=Desc)
        db.session.add(new_task)
        db.session.commit()  


    alltodo = tododb.query.all()
    return render_template("index.html", alltodo = alltodo )

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo_delete = tododb.query.get_or_404(id)
    db.session.delete(todo_delete)
    db.session.commit()
    return jsonify({"success": True, "message": "Todo deleted successfully!"})

@app.route("/update/<int:id>",methods = ["GET" ,"POST"])
def update(id):
    todo_update = tododb.query.get_or_404(id)
    if request.method == "POST":
        Title = request.form.get("title")
        Desc = request.form.get("desc")
        todo_update.task = Title
        todo_update.desc = Desc
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo = todo_update )

@app.get("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True)

