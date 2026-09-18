import os
from openai import OpenAI

# Setup client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get user input
print("Paste your article here. When you're done, type DONE on its own line and press Enter:")
lines = []
while True:
    line = input()
    if line.strip() == "DONE":
        break
    lines.append(line)
user_input = "\n".join(lines)

if not user_input.strip():
    print("Please paste some text first!")
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
        print(f"Summarizing chunk {idx} of {len(chunks)}...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text clearly and concisely."},
                {"role": "user", "content": f"Summarize this text:\n{chunk}"}
            ]
        )
        final_summary += response.choices[0].message.content + " "

    print("\nDone! Here's your summary:\n")
    print(final_summary.strip())