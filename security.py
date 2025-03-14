import streamlit as st
import re

# Set page configuration
st.set_page_config(page_title="Password Strength Checker", layout="wide")

# Apply CSS to change background color
st.markdown(
    """
    <style>
        /* Background color change */
        [data-testid="stAppViewContainer"] {
            background-color:  #D3D3D3;
        }

        /* Remove top padding and margin */
        [data-testid="stHeader"] {
            display: none;
        }

        /* Password strength meter */
        .strength-bar {
            height: 10px;
            border-radius: 5px;
            margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.title("Password Strength Checker!🛡️ ")

st.write("Analyze your password's security level.")

# Password input
password = st.text_input("Enter your password", type="password")

# Variables for password checking
feedback = []
score = 0

if password:
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 **Password should be at least 8 characters long.**")

    # Uppercase & Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔹 **Include both uppercase and lowercase letters.**")

    # Digit Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔹 **Add at least one digit (0-9).**")

    # Special Character Check
    if re.search(r'[&_$%@!#-]', password): 
        score += 1
    else:
        feedback.append("🔹 **Use at least one special character (&_-$%@!#).**")

    # Password Strength Evaluation
    strength_colors = {0: "red", 1: "orange", 2: "yellow", 3: "lightgreen", 4: "green"}
    strength_labels = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}

    st.markdown(f"""
        <div class="strength-bar" style="width: 100%; background: {strength_colors[score]};"></div>
        <p style="text-align: center; font-weight: bold;">{strength_labels[score]}</p>
    """, unsafe_allow_html=True)

    if score == 4:
        st.success("✅ Strong Password! Your password is highly secure.")
    elif score == 3:
        st.warning("⚠️ Good Password! But it can be improved.")
    else:
        st.error("❌ Weak Password! Consider making it stronger.")

    # Improvement Suggestions
    if feedback:
        st.markdown("### 🔍 Improvement Suggestions")
        for tip in feedback:
            st.write(f"- {tip}")

    # Password Suggestions
    if score < 3:
        st.markdown("### 🔑 Suggested Strong Passwords")
        suggestions = [
            "P@ssw0rd!2024",
            "S3cur3#C0d3",
            "My$afeKey987",
            "Str0ng_P@ss!",
            "R@nd0m!Xyz78"
        ]
        for sug in suggestions:
            st.code(sug, language="text")

    # Copy Password Button
    if st.button("📋 Copy Password"):
        st.write("Password copied to clipboard! (This requires JavaScript in real apps)")
else:
    st.info("ℹ️ Please enter your password to check its strength.")
