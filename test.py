import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Customer Service Bot for a restaurant: What are your hours?",
        max_tokens=50,
        temperature=0.7
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print("Error:", e)
