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
    # "response_mime_type": "text/plain",
}
# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
# ]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    # safety_settings=safety_settings,
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
    

    prompt = st.text_area("Enter your prompt:", "I have been predicted with a risk of getting TYPE II diabetes, generate me a table structured wellness plan to reduce the risk")

    if st.button("Generate Response"):
        response = generate_response(prompt)
        st.subheader("Generated Response")
        st.write(response)

if __name__ == "__main__":
    main()
