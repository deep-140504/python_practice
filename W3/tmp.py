import openai

# Set your OpenAI API key
openai.api_key = "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"

def get_billing_usage():
    try:
        # Fetch billing usage details (This is for OpenAI's billing)
        billing = openai.Billing.retrieve()
        
        print("Billing Usage Data:")
        print(billing)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_billing_usage()
