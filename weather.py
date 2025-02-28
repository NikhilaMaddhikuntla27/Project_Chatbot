import requests
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
patterns = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm great! How about you?"]),
    (r"what is your name?", ["I am a chatbot!", "You can call me ChatBot."]),
    (r"bye", ["Goodbye!", "See you later!"]),
]

# Create chatbot instance
chatbot = Chat(patterns, reflections)

def get_weather(city):
    """Fetches the current weather for a given city using WeatherStack API."""
    api_key = "82dd36be792774eac53500daa9cec981"  # Replace with a secure method like environment variables
    base_url = "http://api.weatherstack.com/current"
    complete_url = f"{base_url}?access_key={api_key}&query={city}"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an HTTP error if one occurs
        data = response.json()

        if "current" in data:
            temperature = data["current"].get("temperature")
            return f"The temperature in {city} is {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather details. Please check the city name."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

def start_chat():
    """Starts the chatbot and allows interaction with the user."""
    print("Hello! I am a chatbot. You can ask me general questions or request the weather (e.g., 'weather in London'). Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()  # Get input and normalize case
        
        # Exit condition
        if user_input == 'bye':
            print("Goodbye! Have a great day.")
            break

        # Check if the user asked for the weather
        if user_input.startswith("weather in "):
            city = user_input.replace("weather in ", "").strip()
            response = get_weather(city)
        
        else:
            # Get chatbot's response
            response = chatbot.respond(user_input) or "I'm not sure how to respond to that."

        # Print chatbot response
        print(f"Chatbot: {response}")

# Start the chatbot
start_chat()
