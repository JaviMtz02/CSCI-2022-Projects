from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")

@app.route('/user/<name>')
def greet(name):
  return f'<p>Hello, {name}!'
  
@app.route("/about")
def about():
  return render_template("about.html")

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
  name = None
  if request.method == 'POST':
    name = request.form['name']

  return render_template('form.html', name=name)
  


app.run(host='0.0.0.0', port=81)
