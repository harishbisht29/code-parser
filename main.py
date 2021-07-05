from flask import Flask, jsonify, render_template, request
from Analyzer import analyze_sas_program
app = Flask(__name__)

@app.route('/')
def search():
    return render_template('index.html')

@app.route('/analyze/', methods = ['POST'])
def analyze_program():
    location = request.form['search']
    res= analyze_sas_program(location)
    return render_template('analysis.html', context= res, location=location)
    # return f"Hey you want a {location}"

if __name__ == "__main__":
    app.run(debug=True) 