import re
from transformers import pipeline

# Load the summarization and response generation models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
response_generator = pipeline('text2text-generation', model='facebook/bart-large-cnn')

# Preprocessing function to clean email
def clean_email(email):
    if isinstance(email, str):
        # Remove unnecessary parts (e.g., signatures, metadata)
        email_body = email.split('--')[0]
        email_body = re.sub(r'^.*?\n\n', '', email_body, flags=re.DOTALL)  # Remove headers
        return email_body.strip()
    return ''  # Return empty string for non-string inputs

# Summarization function
def summarize_email(email_text):
    cleaned_email = clean_email(email_text)
    if len(cleaned_email) > 1024:
        cleaned_email = cleaned_email[:1024]  # Truncate if too long
    summary = summarizer(cleaned_email, max_length=80, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Response generation function
def generate_email_response(email_text):
    cleaned_email = clean_email(email_text)
    prompt = f"Reply to the following email:\n\n{cleaned_email}\n\nResponse:"
    response = response_generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

