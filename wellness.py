import streamlit as st

import os
import google.generativeai as genai
genai.configure(api_key=os.environ["AIzaSyB8uoIfZXQ_OACvSTFCJ1tXGa-qSFMrWmg"])
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
def generate_prescription(name, diagnosis, age, sex, weight, current_medications, allergies, coexisting_conditions):
    prompt = f"""Act as a Medical profession. Use Name: {name}\nDiagnosis: {diagnosis}\nAge: {age} years\nSex: {sex}\nWeight: {weight} 
            kg\nCurrent Medications: {current_medications}\nAllergies: {allergies}\nCoexisting Conditions: {', '.join(coexisting_conditions)}
            \n\nUse it and Prescribe medications in the following format\n\n\n Output Format:\nName\n\nAge\n\nWeight\n\Medicine name\n DosageFrequency
            \nInstructions \nPrecautions(if any).Make it in 400 words in proper output format with proper name of medicine"""

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600
    )

    prescription = response['choices'][0]['text']
    return prescription


st.title("Wellness plan generator")

name = st.text_input("Name:")
riskofdisease  = st.text_area("Describe your condition here in detail. Also mention the severity of your condition:")
age = st.number_input("Age:")
sex = st.radio("Sex:", ["Male", "Female"])

allergies = st.text_area("Any Allergies? Please mention here:")
coexisting_conditions = st.multiselect("Coexisting Conditions:", 
                                      ["Pregnancy or Breastfeeding", "Hypertension (high blood pressure)", 
                                       "Diabetes", "Obesity", "Cardiovascular diseases", 
                                       "Respiratory diseases", "Chronic kidney disease", 
                                       "Arthritis and musculoskeletal disorders", "Mental health disorders", 
                                       "Gastrointestinal disorders", "Thyroid Disorders"])

if st.button("Generate Wellness plan"):
    if name and diagnosis and age and weight:
        prescription = generate_prescription(name, diagnosis, age, sex, weight, current_medications, allergies, coexisting_conditions)
        st.text("Prescription:")
        st.write(prescription)
        
    else:
        st.warning("Please fill in all the required information.")

    