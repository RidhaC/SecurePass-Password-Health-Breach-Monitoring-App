from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
from utils import password_score, check_breach

app = Flask(__name__)
CORS(app)  # ✅ Add this

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
