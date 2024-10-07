from flask import Flask, render_template, url_for, request, jsonify

from main import Speller

app = Flask(__name__)

speller = Speller(threshold=3)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/get_correction', methods=['POST'])
def run_function():
    text = request.form.get('text')
    if text:
        text = text.lower()
    data = speller.get_candidates(text)

    corrected_text = data if data else 'correct'
    return render_template('index.html', corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)