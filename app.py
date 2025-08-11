


from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index(): 
    # Read data from the file
    data = [] 
    with open("data.json", "r") as f: 
        for line in f: 
            data.append(json.loads(line))
    return render_template("index.html", data=data[-10:])  # The Last 10 entries 

if __name__ == "__main__":
    app.run(debug=True)
