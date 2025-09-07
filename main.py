from openai import OpenAI
import argparse

def main():
    parser = argparse.ArgumentParser(description="LiteLLM Endpoint Verifier")
    parser.add_argument("--api-key", required=True, help="Your LiteLLM API Key")
    parser.add_argument("--base-url", required=True, help="Base URL for the LiteLLM API")
    args = parser.parse_args()

    client = OpenAI(api_key=args.api_key, base_url=args.base_url)

    try:
        models = client.models.list()
        print("\nAvailable Models:")
        for model in models:
            print(f"  - {model.id}")
        print("\nLiteLLM endpoint is valid and reachable.")
    except Exception as e:
        print(f"\nError connecting to LiteLLM endpoint: {e}")

if __name__ == "__main__":
    main()