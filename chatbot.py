#Python: General-purpose programming language.
#NLTK: Natural Language Toolkit, a library for processing and working with human language data.
#Import the necessary modules from NLTK and set up some initial configurations.
#Step 1: Install Required Libraries
#Step 2: Import Libraries and Initialize NLTK
import nltk
from nltk.chat.util import Chat, reflections 

##Chat: A class from NLTK used to create and manage a simple chatbot.
#Reflections: A dictionary that maps pronouns like "I" to "you" and "me" to "you", which helps in creating responses.

# Download NLTK resources if not already installed
nltk.download('punkt')
#Step 3: Define Pairs (Patterns and Responses)
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you today?"]),
    (r"how are you?", ["I'm doing great, thank you for asking!", "I'm good, how about you?"]),
    (r"what is your name?", ["I am a chatbot created by you!", "I am your friendly assistant!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]),
    (r"(.*) your name?", ["My name is Chatbot."]),
    (r"what can you do?", ["I can answer simple questions like 'What is your name?' or 'How are you?'"]),
    (r"(.*) (location|city|place)?", ["I'm from the digital world!"]),
    (r"how is the weather?", ["I don't know the current weather, but it's always sunny in the digital world!"]),
    (r"(.*)", ["Sorry, I didn't quite understand that. Can you try again?"])
]

#A regular expression pattern (e.g., r"hi|hello|hey"), which defines the kind of input that triggers a response.
#A response (or list of responses), which the bot will use when it matches the input.

#Step 4: Create the Chatbot Class
#Now, we can use the Chat class from NLTK to create the chatbot. You will also use the reflections dictionary, which helps map pronouns like "I" to "you" and vice versa.

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start chatting with the chatbot
def start_chat():
    print("Hello! I am a chatbot. Type 'bye' to exit.")
    while True:
        # Get user input
        user_input = input("You: ") #input(): The chatbot waits for the user’s input.
        
        # If user wants to exit
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break
        
        # Get chatbot's response
        response = chatbot.respond(user_input) #chatbot.respond(user_input): It processes the input using the predefined patterns and provides a suitable response.
        
        # Print chatbot response
        print(f"Chatbot: {response}")

# Start the chatbot
start_chat()


##Step 5: Test the Chatbot
#After defining the start_chat function, you can run your Python script. The chatbot will greet you and wait for you to type something.