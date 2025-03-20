import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! How can I help?']),
    (r'bye|exit|quit', ['Goodbye! Have a great day!', 'See you later!']),
    (r'what is your name?', ['I am a chatbot created with NLTK.', 'I am your friendly chatbot.']),
    (r'how are you?', ['I am just a chatbot, but I am functioning well!', 'I am doing great! Thanks for asking.']),
    (r'(.*) your name?', ['I am a chatbot created with NLTK.', 'I do not have a name, but you can call me Chatbot.']),
    (r'(.) help (.)', ['I can assist you with various queries. What do you need help with?']),
    (r'what is (.*)', ['Can you clarify what you are asking about? I am happy to help.']),
    (r'(.*)', ['I am sorry, I didn’t understand that. Could you please rephrase?'])
]

# Create the chatbot with the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def start_chat():
    print("Hello! I am your chatbot. Type 'exit' or 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__== "__main__":
    start_chat()
