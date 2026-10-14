# 🧠 EvalWise — AI Response Evaluation Tool

**A human-in-the-loop evaluation dashboard for comparing, scoring, and reviewing AI-generated responses.**

EvalWise is a Python-based web application that helps reviewers evaluate two AI-generated responses to the same prompt using a structured scoring rubric. It supports consistent quality assessment, issue tagging, reviewer notes, and evaluation data export.

## ✨ Features

- **Side-by-Side Comparison:** Compare two AI responses to the same prompt.
- **Multi-Dimensional Scoring:** Rate responses from 1–5 across five evaluation criteria.
- **Quality Evaluation Rubric:** Assess helpfulness, relevance, clarity, factual consistency, and instruction following.
- **Issue Detection:** Flag unsupported claims, irrelevant content, contradictions, and other response quality issues.
- **Preferred Response Selection:** Record the preferred answer with a written justification.
- **Reviewer Information:** Capture reviewer IDs and additional notes.
- **Evaluation Metrics:** Track saved evaluations and compare response scores.
- **Visual Analytics:** View score comparisons through charts.
- **Data Export:** Export evaluation records in CSV and JSON formats.
- **Interactive Interface:** Review and score responses through a Streamlit dashboard.

## 🖥️ Screenshots

<img width="1364" height="727" alt="image" src="https://github.com/user-attachments/assets/dfa7a281-cb67-445c-b795-9b2cee600b98" />


<br><br>

<img width="1365" height="725" alt="image" src="https://github.com/user-attachments/assets/47e69cbc-9f79-4950-98ad-69cba752ec8f" />

<br><br>

<img width="1363" height="724" alt="image" src="https://github.com/user-attachments/assets/0c769b7d-53d3-4375-8cc7-5e8ee6d9b803" />

<br><br>

<img width="1363" height="726" alt="image" src="https://github.com/user-attachments/assets/8427a798-1a38-4350-896d-4eea9c07ca9e" />

<br><br>

> Replace the placeholder image URLs with your actual GitHub screenshot URLs. You can also remove any screenshot section you don't need.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and evaluation processing |
| Pandas | Data handling and evaluation metrics |
| Streamlit | Interactive web dashboard |
| CSV | Tabular evaluation data export |
| JSON | Structured evaluation data export |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
ai-response-evaluation-tool/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer
- pip package manager
- Visual Studio Code or another Python editor

### 1. Clone the repository

```bash
git clone https://github.com/DTfrezer/ai-response-evaluation-tool.git
cd ai-response-evaluation-tool
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the environment's Python executable directly.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Launch the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 📊 How to Use

1. Launch the EvalWise dashboard.
2. Enter the prompt that was given to the AI.
3. Paste the first response into Response A.
4. Paste the second response into Response B.
5. Score both responses across all five evaluation dimensions.
6. Select the issues identified in either response.
7. Choose the preferred response and provide a rationale.
8. Add reviewer details and optional notes.
9. Save the evaluation.
10. Review the available metrics and charts.
11. Export the evaluation records as CSV or JSON.

## 📋 Evaluation Criteria

| Criterion | What to Evaluate |
|---|---|
| Helpfulness | Does the response solve the user's problem? |
| Relevance | Does it address the prompt without unnecessary content? |
| Clarity | Is it understandable, organized, and well-written? |
| Factual Consistency | Are its claims accurate and supported by available evidence? |
| Instruction Following | Does it follow the user's requirements and constraints? |

Each criterion uses a **1–5 rating scale**, where higher scores indicate stronger performance against that criterion.

## 🔍 Evaluation Guidelines

- Evaluate each response against the original prompt.
- Apply the same rubric to both responses.
- Prioritize factual reliability and verifiable evidence over writing style alone.
- Flag unsupported claims, contradictions, and irrelevant content.
- Provide a concise justification when selecting a preferred response.
- Treat scores as structured human judgments rather than proof of correctness.

## 📤 Exported Data

EvalWise supports exporting evaluation records for further analysis, reporting, and dataset preparation.

- **CSV:** Suitable for spreadsheets and Pandas-based analysis.
- **JSON:** Suitable for structured records and integration with other tools.

## 🚀 Future Improvements

- Persistent storage using SQLite or PostgreSQL.
- Multi-reviewer workflows and reviewer agreement metrics.
- Evaluation history and audit trails.
- Configurable evaluation rubrics.
- Integration with LLM APIs for optional assisted evaluation.
- Evidence-based fact-checking integrations.
- Batch evaluation of larger datasets.

## ⚠️ Limitations

- Evaluation records remain in the current Streamlit session until exported.
- The application does not automatically call an LLM to generate or evaluate responses.
- It does not independently fact-check claims.
- Scores depend on reviewer judgment and the consistency of the evaluation process.
- This project is a portfolio demonstration, not a production-ready multi-user evaluation platform.

## 👨‍💻 Author

**Sarthak Bhosale**

GitHub: [@DTfrezer](https://github.com/DTfrezer)

## 📜 License

No specific open-source license has been declared yet. Add a `LICENSE` file if you intend to distribute the project under a particular license.

---

*Built to demonstrate practical skills in Python development, AI response quality evaluation, structured annotation, data analysis, and interactive dashboard development.*
