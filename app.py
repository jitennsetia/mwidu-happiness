from flask import Flask, render_template, request

app = Flask(__name__)

# Curated psychology & mental awareness facts
MENTAL_FACTS = {
    "calm": "Slow breathing activates the parasympathetic nervous system and helps reduce anxiety within minutes.",
    "breathing": "Deep breathing lowers cortisol levels and sends a safety signal to your brain.",
    "anxiety": "Anxiety is your brain’s threat-detection system working overtime.",
    "stress": "Chronic stress keeps the body in fight-or-flight mode, exhausting the nervous system.",
    "sleep": "Poor sleep increases anxiety sensitivity by up to 60%.",
    "thoughts": "Thoughts are mental events, not facts. You don’t have to believe every thought.",
    "panic": "Panic attacks are intense but not dangerous. They always pass.",
    "control": "Trying to control anxiety often strengthens it. Acceptance weakens it.",
}

DEFAULT_RESPONSE = (
    "Anxiety is a natural response to stress. "
    "It becomes a concern when it is constant or overwhelming. "
    "Gentle awareness and healthy coping strategies can help."
)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None

    if request.method == "POST":
        query = request.form.get("query", "").lower()

        for key, value in MENTAL_FACTS.items():
            if key in query:
                response = value
                break

        if not response:
            response = DEFAULT_RESPONSE

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
