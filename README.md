**Student Exam Score Predictor**

**Objective**:
- **Purpose**: Provide an easy-to-use Streamlit web app that estimates a student's final exam score based on academic, family, school, and personal features. The prediction uses a pre-trained model loaded from `my_model.pkl` and expects feature names and ordering to match the model training.

**Overview**:
- **What it is**: A single-file Streamlit application (`app.py`) that collects student-related inputs, encodes them, constructs a single-row DataFrame, and returns a predicted exam score (0–100).
- **Tech stack**: Python, Streamlit, Pandas, NumPy, joblib (for loading the trained model). See [requirements.txt](requirements.txt) for the concrete dependency list.

**Features**:
- **Interactive UI**: Grouped input sections for Academic Behavior, Family & Home Environment, School Environment, and Personal Profile.
- **Categorical encoding**: Built-in ordinal and binary encoders to match training-time encodings.
- **Engineered features**: Computes `Study_Motivation_Interaction` and `Parental_Education_Involvement` used by the model.
- **Single-click prediction**: Click the `Predict Exam Score` button to compute and display the estimated score.

**Repository Files**:
- **app.py**: Main Streamlit application that builds the form, encodes inputs, constructs the feature DataFrame, loads the model (`my_model.pkl`) and performs predictions.
- **requirements.txt**: Lists Python dependencies required to run the app.
- **my_model.pkl**: Pre-trained model file (NOT included in repo by default). Place it in the project root.

**Input Details & Expected Encodings**:
The app expects specific input fields and encodings. The column names and order must match the model training exactly. The application constructs the following features (names shown as in code):

- **Parental_Involvement**: ordinal — `Low`=0, `Medium`=1, `High`=2
- **Access_to_Resources**: ordinal — `Low`=0, `Medium`=1, `High`=2
- **Family_Income**: ordinal — `Low`=0, `Medium`=1, `High`=2
- **Teacher_Quality**: ordinal — `Low`=0, `Medium`=1, `High`=2
- **Distance_from_Home**: ordinal — `Near`=0, `Moderate`=1, `Far`=2
- **Parental_Education_Level**: ordinal — `High School`=0, `College`=1, `Postgraduate`=2
- **Type_Private**: binary — `Private`=1, `Public`=0
- **Influence_Positive**: binary — `Positive`=1, otherwise 0
- **Female**: binary — `Female`=1, `Male`=0
- **Hours_Studied_Per_Week**: numeric — float (0.0–80.0)
- **Attendance_Percentage**: numeric — float (0.0–100.0)
- **Extracurricular_Activities**: binary — `Yes`=1, `No`=0
- **Sleep_Hours**: numeric — float (0.0–24.0)
- **Internet_Access**: binary — `Yes`=1, `No`=0
- **Tutoring_Sessions_Per_Month**: numeric — float (0.0–30.0)
- **Physical_Activity_Per_Week**: numeric — float (0.0–40.0)
- **Learning_Disabilities**: binary — `Yes`=1, `No`=0
- **Study_Motivation_Interaction**: engineered — `Hours_Studied_Per_Week * Motivation_Level` where `Motivation_Level` mapping is `Low`=0, `Medium`=1, `High`=2
- **Parental_Education_Involvement**: engineered — `Parental_Education_Level * Parental_Involvement`

Example of the mapping dictionaries used inside `app.py`:

```
ordinal_lmh = {"Low": 0, "Medium": 1, "High": 2}
ordinal_distance = {"Near": 0, "Moderate": 1, "Far": 2}
ordinal_parent_edu = {"High School": 0, "College": 1, "Postgraduate": 2}
motivation_map = {"Low": 0, "Medium": 1, "High": 2}
```

**Feature Order**:
The app currently builds a feature dictionary in the following order (this must match the model's training order):

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

**Installation**:

Prerequisites:
- Python 3.8+ recommended.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

**Running the App**:

Start the Streamlit app locally:

```bash
streamlit run app.py
```

Open the provided local URL (usually `http://localhost:8501`) in your browser.

**Usage Guide**:
- Fill in the inputs under the four sections: Student Academic Behavior, Family & Home Environment, School Environment, and Personal Profile.
- Check numeric inputs for sensible ranges.
- Click `Predict Exam Score` to run the prediction. The app will show the predicted score as `Estimated Exam Score: XX.XX / 100`.

**Model File (`my_model.pkl`)**:
- The application expects a pre-trained model file named `my_model.pkl` to exist in the project root. The file is not included in source control by default.
- If the file is missing you'll see an error when the app attempts to load the model. Ensure you place the correct pickle matching the training feature order described above.

**Troubleshooting**:
- Error while predicting: often caused by mismatched feature names or ordering between `input_df` and the model training data. Verify the feature list and ordering.
- `FileNotFoundError` for `my_model.pkl`: place the model file in the project root or update the path in `app.py`.
- Version mismatches (scikit-learn, joblib) can cause unpickling errors. If you encounter `pickle`/`joblib` errors, recreate the model pickle using the same package versions listed in `requirements.txt`.

**Security & Privacy**:
- This app runs locally and does not transmit data externally by default. Do not upload sensitive student data to public servers without proper controls.

**Extending the App**:
- To swap models, replace `my_model.pkl` with a new pickle trained on the same feature schema and ordering.
- To log predictions or add persistence, integrate a lightweight database (SQLite) or add CSV export.

**Contributing**:
- Fork the repository, make changes, and submit a pull request. For changes that affect feature names, update the README and ensure the model artifact is retrained accordingly.

**License & Credits**:
- Specify your preferred license here (e.g., MIT). Credit any external resources or datasets used during training.

**Contact**:
- For questions or support, add your preferred contact details or a GitHub profile link.

---

This README is crafted to be a complete, professional reference for running, understanding, and maintaining the Student Exam Score Predictor Streamlit app. Replace placeholders (model file, license, contact) with project-specific details before publishing.
