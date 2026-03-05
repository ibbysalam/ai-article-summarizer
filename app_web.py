import os
from openai import OpenAI
import streamlit as st

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit title
st.title("📝 AI Article Summarizer")

# Text area for user input
user_input = st.text_area("Paste your article here:")

# Summarize button
if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please paste some text first!")
    else:
        # Clean the text
        text_to_summarize = user_input.strip().replace("\n", " ")

        # Chunking for long articles
        max_chunk_size = 500
        words = text_to_summarize.split()
        chunks = [" ".join(words[i:i+max_chunk_size]) for i in range(0, len(words), max_chunk_size)]

        # Summarize each chunk
        final_summary = ""
        for idx, chunk in enumerate(chunks, start=1):
            st.info(f"Summarizing chunk {idx} of {len(chunks)}...")
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text clearly and concisely."},
                    {"role": "user", "content": f"Summarize this text:\n{chunk}"}
                ]
            )
            final_summary += response.choices[0].message.content + " "

        st.success("Done! Here’s your summary:")
        st.write(final_summary.strip())