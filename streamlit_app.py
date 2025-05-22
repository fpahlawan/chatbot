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
            model="gpt-3.5",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        st.write("### 🤖 Response:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
