from flask import Flask, render_template, request
from asosoft import G2P, Normalize, Number2Word, PoemClassifier, Sort
from asosoft import Transliteration

app = Flask(__name__)

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('index.html'), 405

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/werger', methods=['POST'])
def cevir():
    hilbijartina_alfabeye = request.form['hilbijartina_alfabeye']
    nivis = request.form['nivis']

    if hilbijartina_alfabeye == "1":
        nivisa_wergerandi = Transliteration.Ar2La(nivis)
    elif hilbijartina_alfabeye == "2":
        nivisa_wergerandi = Transliteration.La2Ar(nivis)
    else:
        return "Hilbijartina nederbasdar.Ji kerema xwe 1 an 2 binivîse."

    return render_template('werger.html', nivisa_wergerandi=nivisa_wergerandi)

if __name__ == '__main__':
    app.run(debug=True)
