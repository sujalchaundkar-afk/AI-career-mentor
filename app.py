from flask import Flask, request, jsonify, send_from_directory
from career import get_career

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/career", methods=["POST"])
def career():
    data = request.get_json()

    skills = data["skills"]
    interest = data["interest"]

    answer = get_career(skills, interest)

    return jsonify({
        "career": answer
    })

if __name__ == "__main__":
    app.run(debug=True)
