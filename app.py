from flask import Flask, render_template, request

app = Flask(__name__)


filepath = "~/static/aboutMe.txt"

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
    return render_template('form.html', name=name)

# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)
