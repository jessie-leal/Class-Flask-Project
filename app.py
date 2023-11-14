from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#setup app to use an SQLalchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampledb.db'
db = SQLAlchemy(app) #database attached to app

#setup a simple table for database
class Visitor(db.Model):
    # need to put what type of data is in each column, and set unique value as primary key
    username = db.Column(db.String(100), primary_key = True)
    numVisits = db.Column(db.Integer, default = 1)

    def __repr__(self):
        return f"{self.username} - {self.numVisits}"

#Create tables in Database
with app.app_context():
    db.create_all()


filepath = "static/aboutMe.txt"

# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Make a homepage
@app.route('/')
def homepage():
    aboutme = readDetails(filepath)
    return render_template('base.html', name="Jessie", aboutMe = aboutme)

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', Sname=name, nameList=listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['name']
        #Check if user is in the database
        visitor = Visitor.query.get(name)
        #if it doesn't find the name, visitor will be "none"
        if visitor == None:
            #Add the Visitor to the database
            visitor = Visitor(username = name) #create the visitor object
            #add visitor to the database
            db.session.add(visitor)
        else:
            visitor.numVisits += 1

        db.session.commit()

    return render_template('form.html', name=name)

@app.route('/visitors')
def visitors():
    #query the database to find all visitors
    people = Visitor.query.all()
    return render_template('visitors.html', people = people)


# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)
