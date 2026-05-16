import sqlite3

DB_NAME = "health_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, age INTEGER, gender TEXT,
            weight REAL, height REAL, bmi REAL,
            sleep_hours REAL, sleep_rested TEXT, sleep_trouble TEXT,
            exercise_days INTEGER, exercise_duration TEXT, exercise_type TEXT,
            stress_level TEXT, mood_score INTEGER, hobbies TEXT,
            water_glasses INTEGER, sugary_drinks TEXT,
            screen_hours REAL, meals_per_day TEXT,
            sleep_score INTEGER, activity_score INTEGER,
            mental_score INTEGER, hydration_score INTEGER,
            screen_score INTEGER, overall_score INTEGER,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_response(data: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO responses (
            name, age, gender, weight, height, bmi,
            sleep_hours, sleep_rested, sleep_trouble,
            exercise_days, exercise_duration, exercise_type,
            stress_level, mood_score, hobbies,
            water_glasses, sugary_drinks,
            screen_hours, meals_per_day,
            sleep_score, activity_score, mental_score,
            hydration_score, screen_score, overall_score
        ) VALUES (
            :name, :age, :gender, :weight, :height, :bmi,
            :sleep_hours, :sleep_rested, :sleep_trouble,
            :exercise_days, :exercise_duration, :exercise_type,
            :stress_level, :mood_score, :hobbies,
            :water_glasses, :sugary_drinks,
            :screen_hours, :meals_per_day,
            :sleep_score, :activity_score, :mental_score,
            :hydration_score, :screen_score, :overall_score
        )
    ''', data)
    conn.commit()
    conn.close()