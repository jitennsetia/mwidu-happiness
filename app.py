from flask import Flask, render_template, request

# IMPORT DATA FIRST (IMPORTANT)
from data import questions, answers

# NLP imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# CREATE VECTORIZER AFTER QUESTIONS EXIST
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english",
    sublinear_tf=True
)

question_vectors = vectorizer.fit_transform(questions)

def search_answer(query):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, question_vectors)
    best_match = similarity.argmax()
    return answers[best_match]

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_query = request.form.get("query")
        if user_query:
            response = search_answer(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    print("🚀 Flask app starting...")
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

