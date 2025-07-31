
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search')
def api_search():
    query = request.args.get("q", "")
    in_stock = request.args.get("inStock", "false").lower() == "true"
    return jsonify([])  # Placeholder: real scraper integration goes here

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
