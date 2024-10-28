from flask import Flask, request, jsonify
from model.model import CovidModel

app = Flask(__name__)

model = None

@app.route("/start_simulation", methods=["POST"])
def start_simulation():
    global model
    config = request.json
    model = CovidModel(num_agents=config["num_agents"], config=config)
    print("Simulation started!")
    return jsonify({"message": "Simulation started!"})

@app.route("/step", methods=["POST"])
def step():
    global model
    if model:
        model.step()
        return jsonify({"message": "Step executed!"})
    return jsonify({"error": "Simulation not started."}), 400

if __name__ == "__main__":
    app.run(debug=True)
