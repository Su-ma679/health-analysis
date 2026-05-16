from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db, save_response
from scoring import calculate_all_scores

app = Flask(__name__)
app.secret_key = "health_analysis_secret_key_2024"

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        form_data = request.form.to_dict()
        scores = calculate_all_scores(form_data)
        session["scores"] = scores
        session["form_data"] = form_data

        # Save to database
        try:
            save_response({
                "name":            form_data.get("name"),
                "age":             form_data.get("age"),
                "gender":          form_data.get("gender"),
                "weight":          form_data.get("weight"),
                "height":          form_data.get("height"),
                "bmi":             scores["bmi"]["value"],
                "sleep_hours":     form_data.get("sleep_hours"),
                "sleep_rested":    form_data.get("sleep_rested"),
                "sleep_trouble":   form_data.get("sleep_trouble"),
                "exercise_days":   form_data.get("exercise_days"),
                "exercise_duration": form_data.get("exercise_duration"),
                "exercise_type":   form_data.get("exercise_type"),
                "stress_level":    form_data.get("stress_level"),
                "mood_score":      form_data.get("mood_score"),
                "hobbies":         form_data.get("hobbies"),
                "water_glasses":   form_data.get("water_glasses"),
                "sugary_drinks":   form_data.get("sugary_drinks"),
                "screen_hours":    form_data.get("screen_hours"),
                "meals_per_day":   form_data.get("meals_per_day"),
                "sleep_score":     scores["sleep"]["score"],
                "activity_score":  scores["activity"]["score"],
                "mental_score":    scores["mental"]["score"],
                "hydration_score": scores["hydration"]["score"],
                "screen_score":    scores["screen"]["score"],
                "overall_score":   scores["overall"]["score"],
            })
        except Exception as e:
            print(f"DB save error: {e}")

        return redirect(url_for("dashboard"))
    return render_template("questionnaire.html")

@app.route("/dashboard")
def dashboard():
    scores = session.get("scores")
    if not scores:
        return redirect(url_for("questionnaire"))
    return render_template("dashboard.html", data=scores)

if __name__ == "__main__":
    app.run(debug=True)