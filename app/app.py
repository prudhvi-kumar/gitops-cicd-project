from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to our GitOps CI/CD Project",
        "application": "Employee Management API",
        "version": "1.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/employees")
def employees():
    return jsonify([
        {"id": 1, "name": "Prudhvi", "role": "DevOps Engineer"},
        {"id": 2, "name": "Poultry", "role": "Software Engineer"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
