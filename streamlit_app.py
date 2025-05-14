import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 RiskMind")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT 4 model to generate responses. "
   

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai.api_key = "17lh7nc1dbSmml1y6URAni4GliF7qzU8ECpC9erfFtmiqqTjKsnYc5TW__A8dpGXb4Jvy9hHg3T3BlbkFJvTIblH86Mi55z_iTaoEstTyCPJksSfgqRWpMR1QWUDuMEVBY2b4_kcL70WhccjeOpHj4FrGhEA"





response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(response['choices'][0]['message']['content'])

  