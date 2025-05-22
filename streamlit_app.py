import streamlit as st
from openai import OpenAI

st.title("💬 RiskMind Chatbot")
st.write("Melakukan Identifikasi Risiko, Risk Level dan Mitigasi Risiko terhadap Inisiatif Bisnis / Objective Bisnis Unit.")

# Ask for API key and prompt
api_key = "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"
user_input = st.text_input("Type 'Start' please")

if api_key and user_input:
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        st.write("### 🤖 Response:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
