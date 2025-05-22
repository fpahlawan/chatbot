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
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        st.write("### 🤖 Response:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
