from flask import Flask, render_template, request, redirect
import mamdani_kleber
import mamdani_peta
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    timestamp = time.time()
    return render_template("index.html", timestamp=timestamp)

@app.route('/calcula', methods=['GET'])
def calcula():
	dismenorreia = int(request.args.get('dismenorreia'))
	dispareunia = int(request.args.get('dispareunia'))
	dorcp = int(request.args.get('dorcp'))
	cansaco = int(request.args.get('cansaco'))
	mamdani_kleber.mamdani_defuzz(dismenorreia, dispareunia, dorcp, cansaco)
	return redirect("http://endometriose.pythonanywhere.com/", "302")

@app.route('/peta')
def hello_world_peta():
    timestamp = time.time()
    return render_template("index_peta.html", timestamp=timestamp)

@app.route('/calculaPeta', methods=['GET'])
def calculaPeta():
	dismenorreia = int(request.args.get('dismenorreia'))
	dispareunia = int(request.args.get('dispareunia'))
	dorcp = int(request.args.get('dorcp'))
	cansaco = int(request.args.get('cansaco'))
	mamdani_peta.mamdani_defuzz(dismenorreia, dispareunia, dorcp, cansaco)
	return redirect("http://endometriose.pythonanywhere.com/peta", "302")