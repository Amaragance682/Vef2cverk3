from flask import Flask, render_template json
import urllib.request





@app.route('frjett/<id>')
def news(id):
    return render_template('frett.html', frjettir=frjettir, id=id)

with urllib.request.urlopen("hhtp://apis.is/currency/") as url:
    data = json.loads(url.read().decode())


@app.route('/gengi')
def currency():
    return render_template('gengi.html', data=data)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'),404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'),500

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/ktsida/<kt>')
def ktsum(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html' , kt=kt , summa=summa)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)