
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Career Mentor</h1>
    <p>Backend is running successfully.</p>
    <p>Frontend page will be connected later.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
