import streamlit as st

st.title("BMI Calculator 👩‍⚕️")

weight = st.number_input("Enter your weight (in kg)", min_value=1.0)
height = st.number_input("Enter your height (in cms)", min_value=1.0)

height = height / 100

if st.button('Calculate BMI'):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)


    bmi_status = ""

    if bmi < 18.5:
        bmi_status = 'Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_status = 'Normal'
    elif bmi > 24.9 and bmi <= 29.9:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"


    html_code = f"""  
    <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 5px solid orange; margin-top: 20px;">  
        <h3 style="color: #6d4c41;">Your BMI: {bmi}</h3>  
        <p style="font-size: 16px; color: #444;">Health Status: You are <b>{bmi_status}</b>.</p>  
    </div>  
    """
    st.markdown(html_code, unsafe_allow_html=True)




