from flask import Flask, request, jsonify
from crawl4ai import crawl_url

app = Flask(__name__)

@app.route('/extract', methods=['GET'])
def extract():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    try:
        result = crawl_url(url, mode="markdown")
        return jsonify({
            "url": url,
            "title": result["title"],
            "content": result["markdown"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
