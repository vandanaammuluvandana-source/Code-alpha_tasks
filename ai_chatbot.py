def chatbot():
    print("Welcome to AI Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I help you?")
        elif "name" in user:
            print("Chatbot: I am your AI Chatbot.")
        elif "help" in user:
            print("Chatbot: I am here to help you.")
        else:
            print("Chatbot: Sorry, I don't understand.")

if __name__ == " __main__ ":
    chatbot()
