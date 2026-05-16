def calculate_bmi(weight, height_cm):
    """Calculate BMI and return value + category."""
    try:
        h = float(height_cm) / 100
        bmi = round(float(weight) / (h * h), 1)
        if bmi < 18.5:
            category = "Underweight"
            color = "#00c6fb"
        elif bmi < 25:
            category = "Normal"
            color = "#43e97b"
        elif bmi < 30:
            category = "Overweight"
            color = "#fa8231"
        else:
            category = "Obese"
            color = "#f857a6"
        return {"value": bmi, "category": category, "color": color}
    except:
        return {"value": 0, "category": "Unknown", "color": "#fff"}


def score_sleep(data):
    """Score sleep section out of 100."""
    score = 0
    tips = []

    # Q5 - Sleep hours (max 50 points)
    hours = float(data.get("sleep_hours", 7))
    if 7 <= hours <= 9:
        score += 50
    elif 6 <= hours < 7 or 9 < hours <= 10:
        score += 35
        tips.append("💤 Try to get 7–9 hours of sleep for optimal health.")
    else:
        score += 10
        tips.append("🚨 Your sleep duration is too low or too high! Aim for 7–9 hours every night.")

    # Q6 - Feeling rested (max 25 points)
    rested_map = {"Always": 25, "Usually": 20, "Sometimes": 12, "Rarely": 5, "Never": 0}
    r = rested_map.get(data.get("sleep_rested", "Sometimes"), 12)
    score += r
    if r < 15:
        tips.append("😴 You rarely feel rested. Try a consistent sleep schedule and avoid screens before bed.")

    # Q7 - Sleep trouble (max 25 points)
    trouble_map = {"Never": 25, "Rarely": 20, "Sometimes": 12, "Often": 5, "Always": 0}
    t = trouble_map.get(data.get("sleep_trouble", "Sometimes"), 12)
    score += t
    if t < 15:
        tips.append("🌙 Trouble sleeping? Avoid caffeine after 3pm and keep your room dark and cool.")

    return {"score": score, "tips": tips}


def score_activity(data):
    """Score physical activity section out of 100."""
    score = 0
    tips = []

    # Q8 - Exercise days (max 40 points)
    days = int(data.get("exercise_days", 3))
    if days >= 5:
        score += 40
    elif days >= 3:
        score += 30
    elif days >= 1:
        score += 15
        tips.append("🏃 Try to exercise at least 3–5 days a week for better health.")
    else:
        score += 0
        tips.append("🚨 No exercise detected! Even a 20-minute daily walk makes a big difference.")

    # Q9 - Exercise duration (max 35 points)
    duration_map = {
        "more_60": 35, "30_60": 30,
        "15_30": 18, "less_15": 8, "none": 0
    }
    d = duration_map.get(data.get("exercise_duration", "15_30"), 18)
    score += d
    if d < 18:
        tips.append("⏱️ Aim for at least 30 minutes per exercise session.")

    # Q10 - Exercise type (max 25 points)
    ex_type = data.get("exercise_type", "")
    if "None" in ex_type:
        score += 0
        tips.append("🧘 Try starting with light activities like yoga or walking.")
    elif any(x in ex_type for x in ["Running", "Gym", "Sports"]):
        score += 25
    elif any(x in ex_type for x in ["Walking", "Yoga"]):
        score += 15
    else:
        score += 10

    return {"score": min(score, 100), "tips": tips}


def score_mental(data):
    """Score mental health section out of 100."""
    score = 0
    tips = []

    # Q11 - Stress level (max 40 points)
    stress_map = {
        "Never": 40, "Rarely": 32,
        "Sometimes": 22, "Often": 10, "Always": 0
    }
    s = stress_map.get(data.get("stress_level", "Sometimes"), 22)
    score += s
    if s < 22:
        tips.append("🧘 High stress detected! Try meditation, deep breathing, or talking to someone you trust.")

    # Q12 - Mood score (max 35 points)
    mood = int(data.get("mood_score", 6))
    if mood >= 8:
        score += 35
    elif mood >= 6:
        score += 25
    elif mood >= 4:
        score += 15
        tips.append("😐 Your mood seems low. Try spending time outdoors or with friends.")
    else:
        score += 5
        tips.append("😞 Your mood is very low. Please consider speaking to a counselor or trusted adult.")

    # Q13 - Hobbies (max 25 points)
    hobbies_map = {"Multiple": 25, "One": 15, "None": 0}
    h = hobbies_map.get(data.get("hobbies", "One"), 15)
    score += h
    if h < 15:
        tips.append("🎨 Having hobbies greatly reduces stress. Try reading, drawing, music, or any activity you enjoy!")

    return {"score": min(score, 100), "tips": tips}


def score_hydration(data):
    """Score hydration section out of 100."""
    score = 0
    tips = []

    # Q14 - Water glasses (max 60 points)
    glasses = int(data.get("water_glasses", 6))
    if glasses >= 8:
        score += 60
    elif glasses >= 6:
        score += 45
        tips.append("💧 You're close! Try to reach 8 glasses of water per day.")
    elif glasses >= 4:
        score += 25
        tips.append("💧 You need more water! Dehydration causes fatigue and poor focus. Aim for 8 glasses.")
    else:
        score += 5
        tips.append("🚨 Severely low water intake! Drink at least 8 glasses (2 litres) of water daily.")

    # Q15 - Sugary drinks (max 40 points)
    sugar_map = {
        "Never": 40, "Sometimes": 28,
        "Often": 12, "Always": 0
    }
    s = sugar_map.get(data.get("sugary_drinks", "Sometimes"), 28)
    score += s
    if s < 28:
        tips.append("🥤 Cut down on sugary drinks — they cause energy crashes and long-term health issues.")

    return {"score": min(score, 100), "tips": tips}


def score_screen(data):
    """Score screen time and lifestyle section out of 100."""
    score = 0
    tips = []

    # Q16 - Screen hours (max 50 points)
    hours = float(data.get("screen_hours", 3))
    if hours <= 2:
        score += 50
    elif hours <= 4:
        score += 35
        tips.append("📱 Try to keep recreational screen time under 2 hours per day.")
    elif hours <= 6:
        score += 18
        tips.append("📱 High screen time! Take regular breaks using the 20-20-20 rule: every 20 mins, look 20 feet away for 20 seconds.")
    else:
        score += 0
        tips.append("🚨 Excessive screen time can cause eye strain, poor sleep and anxiety. Set daily screen limits!")

    # Q17 - Meals (max 50 points)
    meals_map = {
        "3_regular": 50,
        "2_sometimes_skip": 30,
        "1_often_skip": 10,
        "irregular": 5
    }
    m = meals_map.get(data.get("meals_per_day", "3_regular"), 30)
    score += m
    if m < 30:
        tips.append("🍽️ Skipping meals slows your metabolism and reduces energy. Try to eat 3 balanced meals daily.")

    return {"score": min(score, 100), "tips": tips}


def get_badge(score):
    """Return badge info based on score."""
    if score >= 85:
        return {"label": "Excellent",          "color": "#43e97b", "emoji": "🟢"}
    elif score >= 65:
        return {"label": "Good",               "color": "#00c6fb", "emoji": "🔵"}
    elif score >= 40:
        return {"label": "Fair",               "color": "#fa8231", "emoji": "🟡"}
    else:
        return {"label": "Needs Improvement",  "color": "#f857a6", "emoji": "🔴"}


def calculate_all_scores(form_data):
    """Master function — runs all scoring and returns full result dict."""
    weight = form_data.get("weight", 70)
    height = form_data.get("height", 170)
    bmi    = calculate_bmi(weight, height)

    sleep    = score_sleep(form_data)
    activity = score_activity(form_data)
    mental   = score_mental(form_data)
    hydration= score_hydration(form_data)
    screen   = score_screen(form_data)

    overall = round(
        (sleep["score"] + activity["score"] + mental["score"] +
         hydration["score"] + screen["score"]) / 5
    )

    return {
        "name":     form_data.get("name", "User"),
        "age":      form_data.get("age", ""),
        "gender":   form_data.get("gender", ""),
        "bmi":      bmi,
        "sleep":    {**sleep,    "badge": get_badge(sleep["score"])},
        "activity": {**activity, "badge": get_badge(activity["score"])},
        "mental":   {**mental,   "badge": get_badge(mental["score"])},
        "hydration":{**hydration,"badge": get_badge(hydration["score"])},
        "screen":   {**screen,   "badge": get_badge(screen["score"])},
        "overall":  {"score": overall, "badge": get_badge(overall)},
    }