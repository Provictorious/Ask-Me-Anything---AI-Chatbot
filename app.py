from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

load_dotenv(".env")

fetcheed_api_key = os.getenv("API_KEY")
ggi.configure(api_key = fetcheed_api_key)

model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.title("Ask Me Anything - AI Chatbot")

user_quest = st.text_input("Type the question that you are haunting for:")
btn = st.button("Click here now!")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)



st.sidebar.markdown("---")
st.sidebar.markdown("Contributor:")
st.sidebar.markdown("Navid Al Faiyaz Provi")
st.sidebar.markdown("Email: navid.provi@quantanite.com")