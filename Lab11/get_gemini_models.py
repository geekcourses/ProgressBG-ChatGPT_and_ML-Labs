import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def list_gemini_models():
    """
    List all available Gemini models using the google-genai SDK.
    """
    # Get API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment or .env file.")
        return

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    print(f"{'Model ID':<40} | {'Display Name'}")
    print("-" * 80)

    try:
        # Fetch and list all available models
        # The models.list() method returns an iterable of model objects
        for model in client.models.list():
            print(f"{model.name:<40} | {model.display_name}")
            
    except Exception as e:
        print(f"An error occurred while fetching models: {e}")

if __name__ == "__main__":
    list_gemini_models()
