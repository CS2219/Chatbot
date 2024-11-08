from flask import Flask, request, jsonify
import openai
import os

# Initialize the Flask app
app = Flask(__name__)

# Your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(user_input):
    try:
        # Use ChatCompletion instead of Completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a customer service assistant for a restaurant."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract the assistant's response
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print("Error:", e)  # This will print the error message to the terminal
        return "Sorry, I'm having trouble connecting. Please try again later."

# Home route to serve a simple response
@app.route('/')
def home():
    return "Welcome to the Restaurant Chatbot API! Use the /chatbot endpoint to interact with the bot."

# Chatbot route to handle POST requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get("message")
    bot_response = generate_response(user_input)
    return jsonify({"response": bot_response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
