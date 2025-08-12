from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("data.json", "r") as f:
        data = json.load(f)  # loads a list of dicts

    recent_data = data[-10:]  # get last 10 entries

    timestamps = [entry["time"] for entry in recent_data]
    ping = [entry["ping_ms"] for entry in recent_data]
    download = [entry["download_mbps"] for entry in recent_data]
    upload = [entry["upload_mbps"] for entry in recent_data]

    return render_template(
        "index.html",
        timestamps=timestamps,
        ping=ping,
        download=download,
        upload=upload,
    )

if __name__ == "__main__":
    app.run(debug=True)
