from flask import Flask, jsonify, send_file
from scraping_tutorial import ejecutar_scraping
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/scrape')
def scrape():
    try:
        data = ejecutar_scraping()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
