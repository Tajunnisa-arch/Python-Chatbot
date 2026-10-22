
# Task 3: Basic Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thank you!"

    elif user_input == "what is your name":
        return "I am a basic chatbot."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# Main program
def main():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break

    print("Chatbot session ended.")


# Run the chatbot
main()
