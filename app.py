from flask import Flask, request, jsonify
from career import get_career

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Career Mentor Backend is Running"

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
