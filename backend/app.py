from flask import Flask, request, jsonify
from flask_cors import CORS
from questions import questions
from llms import openai_handler, grok_handler, claude_handler, gemini_handler

app = Flask(__name__)
CORS(app)

# GET list of questions
@app.route("/api/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

# POST request with selected question + models
@app.route("/api/compare", methods=["POST"])
def compare_models():
    data = request.json
    question = data.get("question")
    models = data.get("models", [])

    responses = {}
    if "openai" in models:
        responses["OpenAI"] = openai_handler.ask(question)
    if "grok" in models:
        responses["Grok"] = grok_handler.ask(question)
    if "claude" in models:
        responses["Claude"] = claude_handler.ask(question)
    if "gemini" in models:
        responses["Gemini"] = gemini_handler.ask(question)

    return jsonify(responses)

if __name__ == "__main__":
    app.run(debug=True)

