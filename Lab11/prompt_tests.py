import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def auth():
    """ Load environment variables from a .env file located in the same directory.
        Your .env file should contain: GOOGLE_API_KEY="AIzaSy..."
    """
    load_dotenv()

    my_api_key = os.getenv("GOOGLE_API_KEY")

    if not my_api_key:
        print("Error: GOOGLE_API_KEY not found in .env")
        exit()

    return my_api_key


# auth
my_api_key = auth()

# 1. Initialize the Client
client = genai.Client(api_key=my_api_key)

# 2. Define the Task
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config={
            "system_instruction": "You are an HR Consultant specializing in Employee Retention and Organizational Culture."
        },
        contents="""
<context>
    A mid-sized tech company is experiencing a 20% turnover rate among Senior Developers over the last six months. We need to understand why they are leaving.
</context>

<task>
    Draft a set of five targeted exit interview questions designed to uncover systemic issues rather than individual grievances.
</task>

<constraints>
    - Limit to exactly 5 questions.
    - Avoid "yes/no" questions; they must be open-ended.
    - Use a neutral, non-confrontational tone.
    - Do not mention specific names or departments.
</constraints>

<format>
    Present the questions in a numbered list.
    Below each question, include a one-sentence "Objective" explaining what specific insight HR is trying to gain from that query.
</format>
        """
    )

    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")