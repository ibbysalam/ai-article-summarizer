# AI Article Summarizer

A simple command-line tool that takes any chunk of text — a news article, a research paper, a long blog post — and returns a clean, easy-to-read summary using OpenAI's API.

Built as a beginner-friendly project to learn the fundamentals of working with AI APIs: authentication, environment variables, request/response handling, and basic text processing.

## What it does

- Accepts pasted text as input
- Sends it to OpenAI's `gpt-4o-mini` model for summarization
- Automatically chunks long articles so they don't get truncated or fail on token limits
- Prints a clean, combined summary to the terminal

## How it works

<img width="2720" height="2480" alt="article_summarizer_architecture (1)" src="https://github.com/user-attachments/assets/635832c7-7761-4c0c-b08f-4edb70f95d65" />


1. Text is cleaned (extra whitespace and line breaks removed)
2. If the text is long, it's split into ~500-word chunks
3. Each chunk is sent to the model with a system prompt instructing it to summarize clearly and concisely
4. The individual summaries are combined into one final output

## Requirements

- Python 3.x
- An OpenAI account with an API key and billing enabled

## Setup

**1. Install the OpenAI package**

```bash
pip install openai
```

**2. Set your API key as an environment variable**

Never hardcode your API key in the script — treat it like a password.

Mac/Linux:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

Windows (Command Prompt):
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Restart your terminal after setting the key.

**3. Verify it's working**

```bash
python
>>> import os
>>> print(os.getenv("OPENAI_API_KEY")[:4] + "...")
```

If you see the first few characters of your key printed, you're good to go.

## Usage

```bash
python app.py
```

You'll be prompted to paste in your article. Hit Enter, and the summary will print to the terminal.

## Notes

- This project uses the OpenAI API, which is separate from the ChatGPT web app — API usage runs on billed cloud infrastructure, so make sure billing is enabled on your account or you'll hit a `429 insufficient_quota` error.
- This is a CLI tool by design, but the same logic can be extended into a web app, Slack bot, or batch-processing script.

## Possible extensions

- [ ] Loop so users can summarize multiple articles per session
- [ ] Save summaries to a file
- [ ] Handle empty input gracefully
- [ ] Add a simple web interface

## Background

This project was built and documented step-by-step as part of a public learning series on [Towards Data Science](https://towardsdatascience.com/). Read the full walkthrough here: *"I Finally Built My First AI App (And It Wasn't What I Expected)"*

## License

MIT
