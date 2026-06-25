from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

traces = []

# ---------- Middleware ----------
@app.before_request
def start_trace():

    request.trace_id = str(uuid.uuid4())

    request.start_time = datetime.now()


@app.after_request
def end_trace(response):

    duration = (
        datetime.now()
        - request.start_time
    ).total_seconds()

    traces.append({
        "trace_id": request.trace_id,
        "path": request.path,
        "method": request.method,
        "status": response.status_code,
        "duration": duration,
        "timestamp": str(datetime.now())
    })

    response.headers[
        "X-Trace-ID"
    ] = request.trace_id

    return response


# ---------- API ----------
@app.route("/")
def home():

    return jsonify({
        "message":
        "Tracing Enabled"
    })


@app.route("/users")
def users():

    return jsonify({
        "users":
        ["Rahul", "Amit"]
    })


@app.route("/orders")
def orders():

    return jsonify({
        "orders":
        [101, 102]
    })


# ---------- View Traces ----------
@app.route("/traces")
def get_traces():

    return jsonify(traces)


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "UP"
    })


if __name__ == "__main__":

    app.run(debug=True)
