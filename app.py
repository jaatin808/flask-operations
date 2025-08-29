from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)		
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"		
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False			


db = SQLAlchemy(app)							
app.app_context().push()

class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.name}"

@app.route('/')
def hello_world():
    employee = Employee(name = "Employee Name", email = "Employee Email")
    db.session.add(employee)
    db.session.commit()
    all_employee = Employee.query.all()
    return render_template('index.html', all_employee = all_employee)
    # return 'Hello, World!'			
    

if __name__ == '__main__':
    app.run(debug=True)