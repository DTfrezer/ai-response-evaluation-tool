import pandas as pd
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="EvalWise | AI Response Review", page_icon="🧪", layout="wide")
st.title("🧪 EvalWise")
st.caption("Structured human evaluation for AI-generated responses")
st.markdown("Compare two answers to the same prompt, score their quality, flag issues, and document a preference.")

CRITERIA = ["Helpfulness", "Relevance", "Clarity", "Factual consistency", "Instruction following"]
ISSUES = ["Unsupported claim", "Irrelevant content", "Instruction-following error", "Contradiction", "Incomplete answer", "Unsafe or inappropriate", "No obvious issue"]

def sample():
    return pd.DataFrame([
        {"prompt":"Explain an API in simple terms.","response_a":"An API is a way for software systems to communicate using agreed rules.","response_b":"An API is a type of computer monitor.","preferred":"A","justification":"A is accurate and concise.","reviewer":"Sample reviewer","notes":"Example record"},
        {"prompt":"What does HTTP 404 mean?","response_a":"It usually means the requested resource was not found.","response_b":"It means the server successfully completed the request.","preferred":"A","justification":"A correctly describes the status code.","reviewer":"Sample reviewer","notes":"Example record"}
    ])

if "reviews" not in st.session_state:
    st.session_state.reviews = []
with st.sidebar:
    st.header("Review session")
    reviewer = st.text_input("Reviewer ID (optional)", value="")
    st.caption("Scores are human judgments. Record evidence in the justification rather than treating scores as objective truth.")
    if st.button("Clear saved session reviews"):
        st.session_state.reviews = []
        st.rerun()

prompt = st.text_area("Evaluation prompt / user question", placeholder="Paste the prompt both responses are answering...", height=100)
left, right = st.columns(2)
with left:
    st.subheader("Response A")
    response_a = st.text_area("Answer A", key="answer_a", height=220, label_visibility="collapsed", placeholder="Paste response A...")
with right:
    st.subheader("Response B")
    response_b = st.text_area("Answer B", key="answer_b", height=220, label_visibility="collapsed", placeholder="Paste response B...")

st.divider()
st.subheader("Quality rubric")
st.caption("Use the same interpretation for both answers. 1 = poor, 5 = excellent.")
scores = {}
a_col, b_col = st.columns(2)
for criterion in CRITERIA:
    st.markdown(f"**{criterion}**")
    ca, cb = st.columns(2)
    with ca:
        scores[f"A_{criterion}"] = st.slider(f"A — {criterion}", 1, 5, 3, key=f"a_{criterion}")
    with cb:
        scores[f"B_{criterion}"] = st.slider(f"B — {criterion}", 1, 5, 3, key=f"b_{criterion}")

c1, c2 = st.columns(2)
with c1:
    issues_a = st.multiselect("Issues in response A", ISSUES, default=[])
with c2:
    issues_b = st.multiselect("Issues in response B", ISSUES, default=[])
preferred = st.radio("Preferred response", ["A", "B", "Tie / neither"], horizontal=True)
justification = st.text_area("Justification (required)", placeholder="Explain why the selected response is better, citing specific evidence...", height=100)
notes = st.text_input("Additional reviewer notes (optional)")
submit = st.button("Save evaluation", type="primary", use_container_width=True)

if submit:
    if not prompt.strip() or not response_a.strip() or not response_b.strip():
        st.error("Enter the prompt and both responses before saving.")
    elif not justification.strip():
        st.error("Add a short justification so the preference is auditable.")
    else:
        record = {
            "evaluation_id": f"EVAL-{len(st.session_state.reviews)+1:04d}",
            "timestamp_utc": datetime.utcnow().isoformat(timespec="seconds"),
            "reviewer": reviewer.strip(),
            "prompt": prompt.strip(),
            "response_a": response_a.strip(),
            "response_b": response_b.strip(),
            **scores,
            "issues_a": "; ".join(issues_a),
            "issues_b": "; ".join(issues_b),
            "preferred": preferred,
            "justification": justification.strip(),
            "notes": notes.strip()
        }
        st.session_state.reviews.append(record)
        st.success(f"Saved {record['evaluation_id']}.")

st.divider()
st.subheader("Session review log")
reviews = pd.DataFrame(st.session_state.reviews)
if reviews.empty:
    st.info("No evaluations saved in this session yet. Complete the form above to create the first record.")
else:
    avg_a = sum(float(reviews[f"A_{c}"].mean()) for c in CRITERIA) / len(CRITERIA)
    avg_b = sum(float(reviews[f"B_{c}"].mean()) for c in CRITERIA) / len(CRITERIA)
    m1, m2, m3 = st.columns(3)
    m1.metric("Evaluations saved", len(reviews))
    m2.metric("Average score — A", f"{avg_a:.2f}/5")
    m3.metric("Average score — B", f"{avg_b:.2f}/5")
    st.dataframe(reviews[["evaluation_id", "reviewer", "preferred", "justification", "issues_a", "issues_b"]], use_container_width=True, hide_index=True)
    st.bar_chart(pd.DataFrame({"Response A": [reviews[f"A_{c}"].mean() for c in CRITERIA],
                               "Response B": [reviews[f"B_{c}"].mean() for c in CRITERIA]}, index=CRITERIA))
    st.download_button("Download evaluation log CSV", reviews.to_csv(index=False).encode("utf-8"),
                       "ai_response_evaluations.csv", "text/csv", type="primary")
    st.download_button("Download full review JSON", reviews.to_json(orient="records", indent=2).encode("utf-8"),
                       "ai_response_evaluations.json", "application/json")
