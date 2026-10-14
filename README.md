# EvalWise — AI Response Evaluation Tool

A human-in-the-loop review app for comparing two AI responses to the same prompt.

## Features
- Side-by-side response comparison
- Five 1–5 scoring dimensions: helpfulness, relevance, clarity, factual consistency, instruction following
- Issue tagging for unsupported claims, irrelevance, contradictions, and more
- Required rationale for the preferred answer
- Reviewer ID and notes
- Session metrics, score comparison chart, CSV and JSON export

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Use Python 3.10+. Paste a prompt and two answers, complete the rubric, and save the evaluation.

## Evaluation guidance
- Judge the response against the actual prompt.
- Prefer verifiable evidence over style alone.
- Flag claims that are unsupported or conflict with known facts.
- Apply the same rubric consistently across responses.
- Treat numeric scores as structured human judgments, not a guarantee of correctness.

## Limitations
Records live in the current Streamlit session until exported. This starter does not call an LLM or automatically fact-check claims.
