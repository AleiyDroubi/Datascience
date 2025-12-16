import gradio as gr
import joblib
import numpy as np

# ------------------------
# Load model and scaler
# ------------------------
LogisticRegression_model = joblib.load("lr_LogisticRegression_model.pkl")
scaler = joblib.load("scaler.pkl")

# ------------------------
# Prediction function with dynamic suggestions
# ------------------------
def predict_depression(
    age,
    work_hours,
    academic_pressure,
    financial_stress,
    study_satisfaction,
    suicidal_thoughts,
    edu_masters,
    sleep_duration,
    diet
):
    features = []

    # Numeric features
    features.append(age)
    features.append(work_hours)

    # Dropdown features (0-5)
    features.append(academic_pressure)
    features.append(financial_stress)
    features.append(study_satisfaction)

    # Binary features
    features.append(1 if suicidal_thoughts == "Yes" else 0)
    features.append(1 if edu_masters == "Yes" else 0)

    # Sleep duration
    if sleep_duration == "Less than 5 hours":
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(1)

    # Diet
    if diet == "Healthy":
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(1)

    features_array = np.array([features])
    features_scaled = scaler.transform(features_array)

    pred = LogisticRegression_model.predict(features_scaled)[0]
    prob = LogisticRegression_model.predict_proba(features_scaled)[0][1]

    # Risk color
    if prob < 0.4:
        color = "green"
        risk = "Low"
    elif prob < 0.7:
        color = "orange"
        risk = "Medium"
    else:
        color = "red"
        risk = "High"

    # Dynamic suggestions
    suggestions = []
    if academic_pressure >= 4:
        suggestions.append("📚 Whoa, your brain must be doing push-ups! Try time management or some mindfulness breathing.")
    elif academic_pressure <= 1:
        suggestions.append("😎 Easy peasy, but remember, a little challenge keeps the mind sharp!")

    if sleep_duration == "Less than 5 hours":
        suggestions.append("😴 Sleep is life! Consider catching more Zzzs to recharge your superhero powers.")
    elif sleep_duration == "More than 8 hours":
        suggestions.append("🌞 Well-rested! Keep rocking that sleep schedule.")

    if work_hours >= 12:
        suggestions.append("💪 That’s a lot of grind! Remember to take short breaks and maybe stretch a little.")

    if financial_stress >= 4:
        suggestions.append("💰 Money matters can be tricky! Try budgeting or a fun side hustle to ease the pressure.")

    if diet == "Unhealthy":
        suggestions.append("🥦 Snacks are fun, but veggies are magical! Try to sneak some greens in.")

    if suicidal_thoughts == "Yes":
        suggestions.append("❤️ Remember: You’re not alone. Reach out to a trusted friend or a professional.")

    if not suggestions:
        suggestions.append("🎉 Keep it up! Your habits look balanced. Stay awesome!")

    prob_text = f"<span style='color:{color}; font-weight:bold; font-size:20px'>{prob:.2f} ({risk} Risk)</span>"
    suggestions_text = "<br>".join(suggestions)

    return f"<h3 style='color:#28443f;'>Depression Status: {pred}</h3>", prob_text, f"<div style='font-size:16px; color:#28443f'>{suggestions_text}</div>"

# ------------------------
# Gradio UI
# ------------------------
with gr.Blocks() as interface:

    # Global CSS with your color theme
    gr.HTML("""
    <style>
        body {background-color:#f2fd7d;}
        .input-column {background-color:#28443f; color:white; padding:20px; border-radius:15px; box-shadow: 2px 2px 12px #aaa; margin:10px;}
        .output-column {background-color:#fff2e6; color:#28443f; padding:20px; border-radius:15px; box-shadow: 2px 2px 12px #aaa; margin:10px;}
        .gr-button {background-color:#f2fd7d; color:#28443f; font-weight:bold; font-size:18px; padding:10px; border-radius:10px;}
        .gr-number, .gr-dropdown, .gr-radio {font-size:16px; color:#000;}
        h2 {color:#f2fd7d;}
    </style>
    """)

    # Title
    gr.HTML("""
    <h2 style="
        text-align:center; 
        color:#f2fd7d;  
        font-size:36px; 
        font-weight:bold; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom:30px;
    ">
    3azima Depression Prediction
    </h2>
    """)

    # Input section
    with gr.Row():
        with gr.Column(elem_classes="input-column"):
            age_input = gr.Number(label="Age", value=18, precision=0, minimum=14)
            work_hours_input = gr.Dropdown(["Choose a value from 0-16"] + list(range(0,17)), label="Work/Study Hours")
            academic_input = gr.Dropdown(["Choose a value from 0-5"] + list(range(0,6)), label="Academic Pressure")
            financial_input = gr.Dropdown(["Choose a value from 0-5"] + list(range(0,6)), label="Financial Stress")
            study_input = gr.Dropdown(["Choose a value from 0-5"] + list(range(0,6)), label="Study Satisfaction")

        with gr.Column(elem_classes="input-column"):
            suicidal_input = gr.Radio(["No", "Yes"], label="Have you ever had suicidal thoughts?")
            edu_input = gr.Radio(["No", "Yes"], label="edu_Masters")
            sleep_input = gr.Radio(["Less than 5 hours", "More than 8 hours"], label="Sleep Duration")
            diet_input = gr.Dropdown(["Healthy", "Unhealthy"], label="What is your diet?")

    predict_btn = gr.Button("Predict")

    # Output section
    with gr.Row():
        with gr.Column(elem_classes="output-column"):
            pred_output = gr.HTML(label="Prediction")
        with gr.Column(elem_classes="output-column"):
            prob_output = gr.HTML(label="Probability")
            suggestions_output = gr.HTML(label="Suggestions")

    # Connect button
    predict_btn.click(
        fn=predict_depression,
        inputs=[age_input, work_hours_input, academic_input, financial_input, study_input,
                suicidal_input, edu_input, sleep_input, diet_input],
        outputs=[pred_output, prob_output, suggestions_output]
    )

interface.launch(share=True)
