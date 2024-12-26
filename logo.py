import streamlit as st
import requests

def submit_form(name, email, logo_details, company_name):
    url = "https://hook.eu2.make.com/41b9wydndncltrjqpc3deup36zdp5qhj"
    data = {
        "name": name,
        "email": email,
        "message": logo_details,
        "Company": company_name
    }
    response = requests.post(url, data=data)
    return response

# Streamlit App Title
st.set_page_config(page_title="Webhook Form", page_icon="📢", layout="centered")

# Add Global CSS
st.markdown(
    """
    <style>
    /* Background Gradient */
    .stApp {
      background-image: linear-gradient(to right, #1a2a6c, #b21f1f, #fdbb2d);
      background-size: cover;
      color: white;
      font-family: Arial, sans-serif;
    }
    /* Styled Card */
    .card {
      background: rgba(255, 255, 255, 0.9);
      color: #333;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
      margin: 20px auto;
      max-width: 500px;
    }
  /* Styled Button */
 .stButton button {
  background: linear-gradient(45deg, #28a745, #218838); /* Green gradient */
  border: none;
  font-weight: bold;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.stButton button:hover {
  background: linear-gradient(45deg, #218838, #28a745); /* Reverse gradient on hover */
  transform: scale(1.05);
}

    </style>
    """,
    unsafe_allow_html=True
)

# Card Container
st.markdown(
    """
    <style>
    .card {
      background: rgba(255, 255, 255, 0.9);
      color: #333;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
      margin: 20px auto;
      max-width: 600px;
      overflow: hidden; /* Ensures animation stays inside the card */
      animation: fadeIn 1s ease-in-out forwards, typing 3s steps(40, end) 1s forwards;
    }
    
    @keyframes typing {
      from {
        width: 0;
      }
      to {
        width: 100%;
      }
    }
    .typing-effect {
      white-space: nowrap;
      overflow: hidden;
      border-right: 3px solid rgba(255, 255, 255, 0.75);
      display: inline-block;
      animation: typing 3s steps(40, end), blink-caret 0.5s step-end infinite;
    }
    @keyframes blink-caret {
      from, to {
        border-color: transparent;
      }
      50% {
        border-color: rgba(255, 255, 255, 0.75);
      }
    }
    </style>
    <div class='card'>
        <h2 class="typing-effect">Make your logo less than a coffee...</h2>
    </div>
    """,
    unsafe_allow_html=True
)


st.title("Submit The Form")

# Form Inputs
with st.form(key="webhook_form"):
    name = st.text_input("", placeholder="Enter your name")
    email = st.text_input("", placeholder="Enter your email")
    logo_details = st.text_area("", placeholder="Provide details about your logo")
    company_name = st.text_area("", placeholder="Enter your company name")
    submit_button = st.form_submit_button(label="Submit")

st.markdown("</div>", unsafe_allow_html=True)

# Handle Form Submission
if submit_button:
    if name and email and logo_details and company_name:
        response = submit_form(name, email, logo_details, company_name)
        if response.status_code == 200:
            st.success("The Logo Sent Your Provide E-mail Address Successfully !!!")
        else:
            st.error("Failed to submit form. Please try again.")
    else:
        st.warning("Please fill out all fields before submitting.")
