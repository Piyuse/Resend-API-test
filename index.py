import os
import resend

resend.api_key = ""

params = {
    "from": "onboarding@resend.dev",
    "to": ["priyapiyuse.gcsj@gmail.com"],  # Changed to your email
    "subject": "Test Email from Resend API",
    "html": "<strong>Hello I am a stranger</strong>",
}

try:
    email = resend.Emails.send(params)
    print(f"Email sent successfully. ID: {email['id']}")
except Exception as e:
    print(f"An error occurred: {str(e)}")