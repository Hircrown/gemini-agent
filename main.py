import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    # print("Hello from gemini-agent!")
    load_dotenv()

    user_prompt = sys.argv[1]
    
    flag = None
    if len(sys.argv) == 3:
        flag = sys.argv[2]

    if not user_prompt:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    elif user_prompt == "--verbose":
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" --verbose')
        print('Example: python main.py "How do I build a calculator app?" --verbose')
        sys.exit(1)


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    if flag == "--verbose":
        print(f"User prompt: {user_prompt}")
        print("Response")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response")
    print(response.text)


if __name__ == "__main__":
    main()