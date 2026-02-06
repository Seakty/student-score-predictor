<!-- prettier, emoji-rich README designed for clarity and friendliness -->

# 📚 Student Exam Score Predictor

**Predict a student's final exam score quickly — beautifully.**

> Friendly, interactive Streamlit app that estimates final exam performance using academic, family, school, and personal features.

---

## 🚀 Quick Links

- Live (local): run the app with `streamlit run app.py`
- Dependencies: see [requirements.txt](requirements.txt)
- App entrypoint: `app.py`
- Model artifact: `my_model.pkl` (place in project root)

---

## ✨ Highlights

- Clean, grouped input sections for rapid data entry
- Built-in encoders for categorical features to match training
- Two engineered features included: study × motivation and parental edu × involvement
- Presets available (in-app) for fast demos
- Friendly UX: tooltips, spinner, progress bar, and celebratory effects

---

## 📋 Table of Contents

1. [Quick start](#-quick-start)
2. [Usage & Tips](#-usage--tips)
3. [Inputs & Encodings (at-a-glance)](#-inputs--encodings-at-a-glance)
4. [Feature order (important)](#-feature-order-important)
5. [Presets & Examples](#-presets--examples)
6. [Troubleshooting](#-troubleshooting)
7. [Development & Contributing](#-development--contributing)
8. [License & Contact](#-license--contact)

---

## 🧭 Quick Start

1. Install requirements:

```bash
python -m pip install -r requirements.txt
```

2. Run locally:

```bash
streamlit run app.py
```

3. Open the URL shown in your terminal (usually `http://localhost:8501`).

Tip: use the sidebar presets to populate example students instantly. 🎛️

---

## 💡 Usage & Tips

- Fill the form under four sections: Academic Behavior, Family & Home Environment, School Environment, Personal Profile.
- Hover over inputs for helpful tooltips (explain what each field means).
- Click **🔮 Predict Exam Score** to compute the estimate. The app displays a result like `Estimated Exam Score: 84.32 / 100`.
- High scores trigger celebratory UI (balloons); good scores show gentle effects. 🎉❄️

---

## 🔢 Inputs & Encodings (at-a-glance)

All inputs are converted to numeric features before prediction. Use the mapping below so your model artifact and `app.py` stay compatible.

- Parental_Involvement: ordinal — `Low` → 0, `Medium` → 1, `High` → 2
- Access_to_Resources: ordinal — `Low` → 0, `Medium` → 1, `High` → 2
- Family_Income: ordinal — `Low` → 0, `Medium` → 1, `High` → 2
- Teacher_Quality: ordinal — `Low` → 0, `Medium` → 1, `High` → 2
- Distance_from_Home: ordinal — `Near` → 0, `Moderate` → 1, `Far` → 2
- Parental_Education_Level: ordinal — `High School` → 0, `College` → 1, `Postgraduate` → 2
- Type_Private: binary — `Private` → 1, `Public` → 0
- Influence_Positive: binary — `Positive` → 1, otherwise 0
- Female: binary — `Female` → 1, `Male` → 0
- Hours_Studied_Per_Week: numeric — float (0.0–80.0)
- Attendance_Percentage: numeric — float (0.0–100.0)
- Extracurricular_Activities: binary — `Yes` → 1, `No` → 0
- Sleep_Hours: numeric — float (0.0–24.0)
- Internet_Access: binary — `Yes` → 1, `No` → 0
- Tutoring_Sessions_Per_Month: numeric — float (0.0–30.0)
- Physical_Activity_Per_Week: numeric — float (0.0–40.0)
- Learning_Disabilities: binary — `Yes` → 1, `No` → 0
- Study_Motivation_Interaction: engineered — `Hours_Studied_Per_Week * Motivation_Level` (Motivation: Low=0, Medium=1, High=2)
- Parental_Education_Involvement: engineered — `Parental_Education_Level * Parental_Involvement`

Example mapping used in code:

```python
ordinal_lmh = {"Low": 0, "Medium": 1, "High": 2}
ordinal_distance = {"Near": 0, "Moderate": 1, "Far": 2}
ordinal_parent_edu = {"High School": 0, "College": 1, "Postgraduate": 2}
motivation_map = {"Low": 0, "Medium": 1, "High": 2}
```

---

## 📌 Feature Order (IMPORTANT)

The DataFrame passed to the model must use the exact column names and order below (this mirrors the training schema):

```
["Parental_Involvement",
 "Access_to_Resources",
 "Family_Income",
 "Teacher_Quality",
 "Distance_from_Home",
 "Parental_Education_Level",
 "Type_Private",
 "Influence_Positive",
 "Female",
 "Hours_Studied_Per_Week",
 "Attendance_Percentage",
 "Extracurricular_Activities",
 "Sleep_Hours",
 "Internet_Access",
 "Tutoring_Sessions_Per_Month",
 "Physical_Activity_Per_Week",
 "Learning_Disabilities",
 "Study_Motivation_Interaction",
 "Parental_Education_Involvement"]
```

If the model throws shape or key errors, check that your `my_model.pkl` was trained with the same order and names.

---

## 🎯 Presets & Example Scenarios

Use these as starting points in the app sidebar presets.

- **Average Student** — Hours: 10, Attendance: 85%, Motivation: Medium, Resources: Medium
- **High Performer** — Hours: 25+, Attendance: 95%+, Motivation: High, Private school
- **At Risk** — Hours: 2, Attendance: 60%, Motivation: Low, Learning disabilities: Yes

---

## 🛠 Troubleshooting

- Model not found: place `my_model.pkl` in the project root or update the load path in `app.py`.
- Unpickling errors: ensure `scikit-learn`/`joblib` versions match those used during model creation.
- Wrong predictions / shape errors: verify feature names & order in the section above.

If you want, I can help pin the exact package versions in `requirements.txt` to avoid unpickle issues.

---

## 🧪 Development notes

- The UI is implemented in `app.py` using Streamlit. It loads the model with `joblib.load("my_model.pkl")`.
- For reproducibility: keep a copy of the training script and the exact package versions used to train the model.

Suggested improvements:
- Add automated unit tests for input → encoded feature mapping.
- Add a CI step that validates `my_model.pkl` against a sample input schema.

---

## 🤝 Contributing

- Found an issue or want a feature? Open an issue or submit a PR. If a change affects feature names or ordering, retrain the model and update this README.

---

## 📝 License & Contact

- Add your preferred license (MIT, Apache, etc.) and contact information here before publishing.

---

Made with ❤️ — polish and test the model artifact before public deployment. Want me to (A) run the app locally, (B) pin `requirements.txt` versions, or (C) add a sample `my_model.pkl` placeholder? Reply with A, B, or C.

