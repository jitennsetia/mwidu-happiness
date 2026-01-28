from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None

    if request.method == "POST":
        query = request.form.get("query", "").lower()

        if "calm" in query:
            response = "Slow breathing, grounding exercises, and focusing on the present moment can help calm anxiety quickly."
        elif "why" in query:
            response = "Anxiety happens when the brain perceives danger and activates the fight-or-flight response."
        elif "symptom" in query:
            response = "Common anxiety symptoms include restlessness, racing thoughts, sweating, and difficulty sleeping."
        else:
            response = (
                "Anxiety is a natural response to stress or perceived danger. "
                "If it becomes constant or overwhelming, professional support can help."
            )

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run()
