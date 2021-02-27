from flask import Flask, request
import os
import logging
import json

log = logging.getLogger()
app = Flask(__name__)

@app.route('/data', methods = ['POST'])
def post_endpoint():
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            data = dict()
        a = data.get("a", 23)
        b = data.get("b", 42)
        return json.dumps({"result": a + b })
    except Exception as e:
        log.error(f"Failed to calculate data. error: {repr(e)}")
        return json.dumps({"error": repr(e)})

@app.route('/version')
def environment_info():
    return json.dumps({"version": "0.0.1"})

@app.route('/ping')
def ping():
    return "PONG"

if __name__ == '__main__':
    app.run(port=8084)