from flask import Flask, request, jsonify
from utils import password_score, check_breach

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")
    return jsonify({
        "score": password_score(password),
        "breached": check_breach(password)
    })

if __name__ == "__main__":
    app.run(debug=True)
