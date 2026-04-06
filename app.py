import streamlit as st

# Page config
st.set_page_config(page_title="Smart BMI Calculator", page_icon="💪", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">💪 Smart BMI Calculator</p>', unsafe_allow_html=True)

st.write("### Enter your details below:")

# Inputs
height = st.slider("Height (cm)", 100, 220, 170)
weight = st.slider("Weight (kg)", 30, 150, 70)

# BMI Calculation
if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)

    st.write(f"## Your BMI: {bmi:.2f}")

    # Category
    if bmi < 18.5:
        st.warning("Underweight ⚠️")
    elif 18.5 <= bmi < 25:
        st.success("Normal weight ✅")
    elif 25 <= bmi < 30:
        st.warning("Overweight ⚠️")
    else:
        st.error("Obese ❌")

    # Progress bar visualization
    progress = min(int(bmi * 2), 100)
    st.progress(progress)