from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Honeypot Fake Project API!"

@app.route("/honeypot", methods=["GET"])
def honeypot():
    return jsonify({"message": "Honeypot endpoint reached successfully!"})

if __name__ == "__main__":
    print("Starting the application...")
    app.run(debug=True)
