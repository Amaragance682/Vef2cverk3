from flask import Flask, render_template, json
import urllib.request
import os
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)

app.jinja_env.add_extension(ext.do)

def format_time(gogn):
    return datetime.strptime(gogn, '%Y-%m-%dT%H:%M.%S.%f').strftime('%d. %m. %Y Kl. %H:%M')

app.jinja_env.add_extension(ext.do)

app.jinja_env.filters['format_time'] = format_time

#bensinstodvar json skra
with urllib.request.urlopen("http://apis.is/petrol/") as url:
    gogn = json.loads(url.read().decode())

#laegsta verdid

def minPetrol():
    minPetrolPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:
        if i['bensin95'] is not None:
            if i['bensin95'] < minPetrolPrice:
                minPetrolPrice = i ['bensin95']
                company = i['company']
                address = i['name']
    return [minPetrolPrice, company, address]


#forsidan
@app.route('/')
def index():
    return render_template('index.html', gogn=gogn, minP=minPetrol() )

@app.route('/company/<company>')
def comp(company):
    return render_template('company.html', gogn=gogn, com=company)

@app.route('/moreinfo/<key>')
def more(key):
    return render_template('moreinfo.html', gogn=gogn, k=key)

@app.route('/gengi')
def currency():
    return render_template('gengi.html', gogn=gogn)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'),404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'),500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)