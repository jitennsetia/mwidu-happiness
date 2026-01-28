from flask import Flask, render_template, request
import random

app = Flask(__name__)

FACTS = {
    "daily": [
        "Anxiety is a false alarm triggered by the brain when it senses danger without real threat.",
        "Fear without reason is common in anxiety and does not mean something bad will happen.",
        "Your nervous system cannot stay anxious forever; it always settles down.",
        "Anxiety symptoms are uncomfortable but not harmful.",
        "Thoughts are not facts, even when they feel intense."
    ],
    "calm": [
        "Slow breathing sends a safety signal to the brain and reduces anxiety.",
        "Grounding techniques help bring attention back to the present moment.",
        "Letting anxiety be present often reduces it faster than fighting it."
    ],
    "why": [
        "Anxiety happens when the brain misinterprets safety signals as danger.",
        "Past experiences can train the brain to overreact to harmless situations.",
        "Anxiety is a protection mechanism working overtime."
    ],
    "symptoms": [
        "Common anxiety symptoms include racing heart, restlessness, and worry.",
        "Physical symptoms of anxiety are caused by adrenaline.",
        "Anxiety symptoms can appear without any external threat."
    ]
}

@app.route("/", methods=["GET"])
def home():
    category = request.args.get("type")

    if category and category in FACTS:
        fact = random.choice(FACTS[category])
        title = category.capitalize().replace("why", "Why Anxiety Happens")
    else:
        fact = random.choice(FACTS["daily"])
        title = "Mental Awareness Fact of the Day"

    return render_template(
        "index.html",
        fact=fact,
        title=title
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
