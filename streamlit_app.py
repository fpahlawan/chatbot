import streamlit as st
import openai

# Streamlit app title and description
st.title("💬 RiskMind")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-4 model to generate responses."
)

# Ask user for their OpenAI API key
api_key = "17lh7nc1dbSmml1y6URAni4GliF7qzU8ECpC9erfFtmiqqTjKsnYc5TW__A8dpGXb4Jvy9hHg3T3BlbkFJvTIblH86Mi55z_iTaoEstTyCPJksSfgqRWpMR1QWUDuMEVBY2b4_kcL70WhccjeOpHj4FrGhEA"

# Get user input
user_input = st.text_input("Ask me anything:")

# Proceed if both API key and input are provided
if api_key and user_input:
    openai.api_key = api_key

    # Call OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Display response
        st.write("### 🤖 Response:")
        st.write(response['choices'][0]['message']['content'])

    except Exception as e:
        st.error(f"Error: {e}")
