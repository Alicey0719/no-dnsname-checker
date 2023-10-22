from flask import Flask, request, jsonify
import logging
import socket

app = Flask(__name__)


@app.route("/resolve-dns", methods=["POST"])
def resolve_dns():
    try:
        data = request.get_json()
        if "domains" not in data:
            return jsonify(error='Invalid JSON format. Missing "domains" key.'), 400

        results = {}
        for domain in data["domains"]:
            try:
                ip_address = socket.gethostbyname(domain)
                if ip_address == "0.0.0.0":
                    results[domain] = None
                else:
                    results[domain] = ip_address
            except socket.gaierror:
                results[domain] = None
        app.logger.info(results)
        response_json = [key for key, value in results.items() if value is None]
        # response_json = jsonify(results)
        return response_json

    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    app.run(host="0.0.0.0", port=52412, threaded=True)
