from flask import Flask, render_template

import urllib.request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

# listi (dicticonary)

frettir = [
    ["0","Fyrirsogn 0","Innihald frettar 0","hofundur 0"],
    ["1","Fyrirsogn 1","Innihald frettar 1","hofundur 1"],
    ["2","Fyrirsogn 2","Innihald frettar 2","hofundur 2"],
    ["3","Fyrirsogn 3","Innihald frettar 3","hofundur 3"],
    ["4","Fyrirsogn 4","Innihald frettar 4","hofundur 4"],
    ["5","Fyrirsogn 5","Innihald frettar 5","hofundur 5"],
] 

@app.route('/ktsida/<kt>')
def ktsum(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html' , kt=kt , summa=summa)

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html' , frettir = frettir)

@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id],nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'),404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'),500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)