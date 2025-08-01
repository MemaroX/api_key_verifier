import google.generativeai as genai
import os

def verify_api_key(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Hello, Gemini!", safety_settings={'HARASSMENT': 'block_none'})
        print("API Key is valid! Response from Gemini:")
        print(response.text)
        return True
    except Exception as e:
        print(f"API Key verification failed. Error: {e}")
        print("Please double-check your API key and ensure it has access to the Generative Language API.")
        return False

def main():
    print("\n--- Google Gemini API Key Verifier ---")
    api_key = input("Please enter your Google Gemini API Key: ")

    if verify_api_key(api_key):
        print("\nVerification successful. Your API key is ready for use.")
    else:
        print("\nVerification failed. Please check the error message above.")

if __name__ == "__main__":
    main()
