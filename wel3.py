import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI with the API key
API_KEY = "AIzaSyB8uoIfZXQ_OACvSTFCJ1tXGa-qSFMrWmg"
genai.configure(api_key=API_KEY)

# Create the generative model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 1048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

# Function to generate response from the model
def generate_response(prompt):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    return response.text

# Streamlit app
def main():
    st.title("Generative AI Response Generator")
    name = st.text_input("Name:")
    riskofdisease = st.text_area("Describe your condition here in detail. Also mention the risk of the condition:")
    age = st.number_input("Age:")
    sex = st.radio("Sex:", ["Male", "Female"])
    weight = st.number_input("Weight (kg):")
    current_medications = st.text_area("Current Medications:")
    allergies = st.text_area("Any Allergies? Please mention here:")
    coexisting_conditions = st.multiselect("Coexisting Conditions:", 
                                      ["Pregnancy or Breastfeeding", "Hypertension (high blood pressure)", 
                                       "Diabetes", "Obesity", "Cardiovascular diseases", 
                                       "Respiratory diseases", "Chronic kidney disease", 
                                       "Arthritis and musculoskeletal disorders", "Mental health disorders", 
                                       "Gastrointestinal disorders", "Thyroid Disorders"])

    prompt = f"""I have been predicted with a risk of getting {riskofdisease}, generate me a table structured wellness plan to reduce the risk using the following:\nName: {name}\nAge: {age} years\nSex: {sex}\nWeight: {weight} kg\nCurrent Medications: {current_medications}\nAllergies: {allergies}\nCoexisting Conditions: {', '.join(coexisting_conditions)}"""

    if st.button("Generate Response"):
        response = generate_response(prompt)
        st.subheader("Generated Response")
        st.write(response)

if __name__ == "__main__":
    main()
