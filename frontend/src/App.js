import React, { useState, useEffect } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);
  const [selectedQuestion, setSelectedQuestion] = useState("");
  const [selectedModels, setSelectedModels] = useState([]);
  const [responses, setResponses] = useState({});

  useEffect(() => {
    axios.get("http://localhost:5000/api/questions")
      .then((res) => {
        setQuestions(res.data);
        setSelectedQuestion(res.data[0] || "");
      })
      .catch((err) => console.error("Failed to load questions:", err));
  }, []);

  const toggleModel = (model) => {
    setSelectedModels((prev) =>
      prev.includes(model)
        ? prev.filter((m) => m !== model)
        : [...prev, model]
    );
  };

  const handleCompare = () => {
    axios.post("http://localhost:5000/api/compare", {
      question: selectedQuestion,
      models: selectedModels,
    })
      .then((res) => setResponses(res.data))
      .catch((err) => console.error("Compare failed:", err));
  };

  return (
    <div className="container min-vh-100 d-flex justify-content-center align-items-center">
      <div className="card">
        <div className="card-body p-5">
          <h1 className="card-title text-center mb-3">
            LLM Statistics Comparator
          </h1>

          <div className="mb-4">
            <div className="mb-2">
              <p>
                <em>Each LLM is prompted with:</em><br />
                <code>"You are a graduate-level statistics tutor. Give me a short concise answer."</code>
              </p>
            </div>

            <label htmlFor="questionSelect" className="form-label">
              Select a Question:
            </label>
            <select
              id="questionSelect"
              className="form-select"
              value={selectedQuestion}
              onChange={(e) => setSelectedQuestion(e.target.value)}
            >
              {questions.map((q, i) => (
                <option key={i} value={q}>
                  {q}
                </option>
              ))}
            </select>
          </div>

          <div className="mb-4">
            <label className="form-label">Select Models:</label>
            <div className="checkbox-group">
              {["openai", "grok", "claude", "gemini"].map((model) => (
                <div className="form-check form-check-inline" key={model}>
                  <input
                    className="form-check-input custom-checkbox"
                    type="checkbox"
                    checked={selectedModels.includes(model)}
                    onChange={() => toggleModel(model)}
                    id={model}
                  />
                  <label
                    className="form-check-label text-capitalize"
                    htmlFor={model}
                  >
                    {model}
                  </label>
                </div>
              ))}
            </div>
          </div>

          <button
            className="btn btn-primary btn-custom mb-5"
            onClick={handleCompare}
          >
            Compare
          </button>

          {Object.keys(responses).length > 0 && (
            <div className="mt-3">
              {Object.entries(responses).map(([model, response]) => {
                const wordCount = response.split(/\s+/).filter(Boolean).length;

                return (
                  <div className="response-card mb-4" key={model}>
                    <div className="card-body">
                      <h6 className="card-title text-center text-capitalize">
                        {model}
                      </h6>

                      <pre className="mb-0 text-center">
                        {response}
                      </pre>

                      <p className="text-center mt-2">
                        <strong>Word Count:</strong> {wordCount}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
