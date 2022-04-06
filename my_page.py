from flask import Flask
from flask import render_template
from flask import request, redirect
app = Flask(__name__)
@app.route("/main")
def greeting():
    return render_template("greeting.html")
@app.route('/form', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       return render_template("form.html")
   elif request.method == 'POST':
       print(request.form)
       return redirect("/main")