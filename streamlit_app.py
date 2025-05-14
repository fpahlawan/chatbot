import streamlit as st
from openai import OpenAI

st.title("💬 RiskMind Chatbot")
st.write("Ask anything and GPT-4 will answer.")

# Ask for API key and prompt
api_key = "17lh7nc1dbSmml1y6URAni4GliF7qzU8ECpC9erfFtmiqqTjKsnYc5TW__A8dpGXb4Jvy9hHg3T3BlbkFJvTIblH86Mi55z_iTaoEstTyCPJksSfgqRWpMR1QWUDuMEVBY2b4_kcL70WhccjeOpHj4FrGhEA"
user_input = st.text_input("Ask a question:")

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