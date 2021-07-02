from os import truncate
from flask import Flask , render_template, request  # importig flask and allowing to render the HTML templete
from flask_sqlalchemy import SQLAlchemy  # For the database which is required to store our todos
from datetime import datetime
app = Flask(__name__)   # Flask constructor
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
  
# A decorator used to tell the application
# which URL is associated function

class Todo(db.Model):                                          # creating the class for database
    sno = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(200), nullable=False )
    desc = db.Column(db.String(500), nullable=False )
    date_created = db.Column(db.DateTime, default = datetime.utcnow )

    def __repr__(self) -> str:   # This ia to show that what do we want to see in the output
        return f"{self.sno} - {self.title}"

    
@app.route('/', methods = ['GET','POST'])                 # we nned to call our POST method request here
def hello():
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)                              # to add the todos to our database
        db.session.commit()                                # commit the changes

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)  
    

@app.route('/show')      
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'Learning FLASK'
  
if __name__=='__main__':                                    # driving program
   app.run(debug=True)                                      # we can also add another parameter such as port to change the PORT