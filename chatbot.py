import re
import datetime
import random

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"])

    # Asking time
    elif re.search(r"\b(time|current time|what time)\b", user_input):
        return f"The current time is {get_time()}."

    # Asking about chatbot
    elif re.search(r"\b(who are you|your name|what are you)\b", user_input):
        return "I'm a simple rule-based chatbot created by Venkatesh!"

    # Asking about weather
    elif re.search(r"\b(weather|temperature|climate)\b", user_input):
        return "I'm not connected to the internet, but it’s always sunny in my code! ☀️"

    # Asking about hobbies
    elif re.search(r"\b(hobby|hobbies|what do you do)\b", user_input):
        return "I enjoy chatting with humans and learning new patterns!"

    # Goodbye
    elif re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye! Have a great day "

    # Fallback response
    else:
        return "I'm not sure how to respond to that. Can you try something else?"

# Running the chatbot
print("Chatbot: Hello! I'm your rule-based chatbot. Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Chatbot:", response)
    if user.lower() in ["bye", "exit", "quit"]:
        break
