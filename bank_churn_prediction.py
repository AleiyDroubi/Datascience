import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df = pd.read_csv('cleaned_data.csv')

#train split data
X = df.drop(['churn','low_credit_score','vip_customer','is_Elderly','InactiveWithoutbalance','IsActiveWithoutbalance','IsActiveWithbalance'],axis=1)
y = df['churn']
X_scaled = scaler.fit_transform(X)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
#LightGBM classifier    
import lightgbm as lgb
tree = lgb.LGBMClassifier(random_state=42,class_weight='balanced')
tree.fit(X_train, y_train)

import gradio as gr
import joblib
import numpy as np
joblib.dump(tree,"lgbmtree.joblib")

# Load your trained model
tree = joblib.load("lgbmtree.joblib")  # Relative path

with gr.Blocks(title="Churn Prediction Dashboard") as demo:
    gr.Markdown("# 🏦 Customer Churn Prediction System")
    gr.Markdown("### Predict which customers are likely to leave")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Customer Details")
            age = gr.Number(label="Age", value=35)
            credit_score = gr.Slider(label="Credit Score", minimum=300, maximum=850, value=650)
            gender = gr.Radio(label="Gender", choices=["Male", "Female"], value="Male")
            
        with gr.Column(scale=1):
            gr.Markdown("### Account Information")
            balance = gr.Number(label="Balance", value=10000)
            product_number = gr.Slider(label="Number of Products", minimum=1, maximum=4, value=1)
            tenure = gr.Slider(label="Tenure (years)", minimum=0, maximum=10, value=2)
    
    with gr.Row():
        estimated_salary = gr.Number(label="Estimated Salary", value=50000)
        active_member = gr.Radio(label="Active Member", choices=["Yes", "No"], value="Yes")
        country = gr.Dropdown(label="Country", choices=["France", "Germany", "Spain"], value="France")
        credit_card = gr.Radio(label="Has Credit Card", choices=["Yes", "No"], value="Yes")
    
    predict_btn = gr.Button("🔮 Predict Churn Risk", variant="primary")
    
    # Custom HTML output container
    output_html = gr.HTML(
        value="<div style='text-align: center; padding: 50px; color: #666;'>Results will appear here</div>"
    )
    
    def predict_and_display(age, credit_score, gender, estimated_salary, balance, 
                            product_number, tenure, active_member, country, credit_card):
        if age < 18 or age > 100:
            return f"""
        <div style="
            padding: 40px;
            background: linear-gradient(135deg, #fff4e5, #ffe0b3);
            border: 4px solid #ff9800;
            border-radius: 16px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            box-shadow: 0 8px 25px rgba(255, 152, 0, 0.25);
            margin: 20px;
        ">
            <div style="font-size: 60px; margin-bottom: 10px; color:#000 ">Warning</div>
            <h2 style="color: #e65100; margin: 15px 0; font-size: 28px;">
                Invalid Customer Age Detected
            </h2>
            <p style="color: #d84315; font-size: 20px; margin: 15px 0;">
                Age must be between <strong style="color:#000">18</strong> and <strong style="color:#000">100</strong> years.
            </p>
            <p style="color: #bf360c; font-size: 24px; font-weight: bold; margin: 20px 0;">
                Current age entered: <span style="background: #ffcc80; padding: 8px 16px; border-radius: 50px; color:#000;">{age}</span>
            </p>
            <p style="color: #78909c; font-size: 16px; margin-top: 20px; line-height: 1.6;">
                This model was trained on real adult bank customers only.<br>
                Ages outside this range are not meaningful for churn prediction.
            </p>
        </div>
        """
        
        # === PREDICTION LOGIC ===
        # Convert categorical inputs to numerical
        gender_num = 1 if gender.lower() == 'male' else 0
        active_num = 1 if active_member.lower() == 'yes' else 0
        credit_card_num = 1 if credit_card.lower() == 'yes' else 0
        
        # Country encoding (one-hot)
        country_france = 1 if country == 'France' else 0
        country_germany = 1 if country == 'Germany' else 0
        country_spain = 1 if country == 'Spain' else 0
        
        # Create features array in EXACT order your model expects
        features = np.array([[
            credit_score,      # 1. credit_score
            gender_num,        # 2. gender
            age,               # 3. age
            tenure,            # 4. tenure
            balance,           # 5. balance
            product_number,    # 6. products_number
            credit_card_num,   # 7. credit_card
            active_num,        # 8. active_member
            estimated_salary,  # 9. estimated_salary
            country_france,    # 10. country_France
            country_germany,   # 11. country_Germany
            country_spain      # 12. country_Spain
        ]])
        
        # Make prediction
        prediction = tree.predict(features)[0]
        probability = tree.predict_proba(features)[0][1]
        
        # === HTML DISPLAY WITH CUSTOM COLORS ===
        if prediction == 1:
            # High risk - Red theme
            main_color = "#d32f2f"
            icon = "⚠️"
            title = "HIGH CHURN RISK"
            bg_color = "#ffebee"
            rec_bg_color = "#fff3e0"
            rec_border = "#ff9800"
            rec_text_color = "#e65100"
            rec_icon = "🔥"
            
            # High risk recommendations
            recommendations = '''
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #f44336;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #f44336; margin-right: 8px;">🔔</span>
                    <strong style="color: #d32f2f;">Immediate Action Required</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Call customer within 24 hours with retention specialist</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #ff9800; margin-right: 8px;">💰</span>
                    <strong style="color: #e65100;">Financial Incentive</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Offer 40% discount on next purchase or service</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #4caf50; margin-right: 8px;">⭐</span>
                    <strong style="color: #388e3c;">Premium Upgrade</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Free premium features for 3 months</div>
            </div>
            '''
            
        else:
            # Low risk - Green theme
            main_color = "#388e3c"
            icon = "✅"
            title = "LOW CHURN RISK"
            bg_color = "#e8f5e9"
            rec_bg_color = "#e3f2fd"
            rec_border = "#2196f3"
            rec_text_color = "#0d47a1"
            rec_icon = "📊"
            
            # Low risk recommendations
            recommendations = '''
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #2196f3; margin-right: 8px;">👁️</span>
                    <strong style="color: #0d47a1;">Standard Monitoring</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Monitor account activity through standard channels</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #673ab7;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #673ab7; margin-right: 8px;">🏆</span>
                    <strong style="color: #4527a0;">Loyalty Program</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Include in loyalty program for retention</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #009688;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="color: #009688; margin-right: 8px;">📧</span>
                    <strong style="color: #00695c;">Communication</strong>
                </div>
                <div style="color: #555; font-size: 14px;">Send quarterly satisfaction survey and updates</div>
            </div>
            '''
        
        # Build the HTML response
        html_response = f"""
        <div style="padding: 25px; border-radius: 12px; background: {bg_color}; border: 3px solid {main_color}; color: #333;">
            <!-- HEADER -->
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <span style="font-size: 42px; margin-right: 15px; color: {main_color};">{icon}</span>
                <div>
                    <h2 style="margin: 0; color: {main_color}; font-size: 28px;">{title}</h2>
                    <div style="color: #666; font-size: 14px; margin-top: 5px;">
                        Based on machine learning analysis of 12 customer features
                    </div>
                </div>
            </div>
            
            <!-- PREDICTION DETAILS -->
            <div style="background: white; padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                <h3 style="margin-top: 0; color: #444; border-bottom: 2px solid {main_color}; padding-bottom: 8px;">📊 Prediction Details</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                    <div style="text-align: center;">
                        <div style="font-size: 13px; color: #777; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Probability</div>
                        <div style="font-size: 48px; font-weight: bold; color: {main_color};">{probability:.1%}</div>
                        <div style="font-size: 12px; color: #999; margin-top: 5px;">Risk Score</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 13px; color: #777; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Prediction</div>
                        <div style="font-size: 32px; font-weight: bold; color: #333; padding: 10px; background: #f5f5f5; border-radius: 8px;">
                            {'WILL CHURN' if prediction==1 else 'WILL STAY'}
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- RECOMMENDED ACTIONS -->
            <div style="background: {rec_bg_color}; padding: 20px; border-radius: 10px; border: 2px solid {rec_border}; margin: 20px 0; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                <div style="display: flex; align-items: center; margin-bottom: 15px;">
                    <span style="font-size: 28px; margin-right: 10px; color: {rec_border};">{rec_icon}</span>
                    <h3 style="margin: 0; color: {rec_text_color};">🎯 Recommended Actions</h3>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr; gap: 12px;">
                    {recommendations}
                </div>
            </div>
            
            <!-- FOOTER NOTE -->
            <div style="margin-top: 20px; padding: 12px; background: rgba(255,255,255,0.8); border-radius: 8px; font-size: 12px; color: #666; text-align: center; border: 1px dashed #ccc;">
                <strong>Model Information:</strong> LightGBM  | {tree.n_features_in_} features | Last updated: Today
            </div>
        </div>
        """
        
        return html_response
    
    predict_btn.click(
        fn=predict_and_display,
        inputs=[age, credit_score, gender, estimated_salary, balance, 
                product_number, tenure, active_member, country, credit_card],
        outputs=output_html
    )

# Launch the interface
demo.launch()