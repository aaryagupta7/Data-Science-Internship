from textblob import TextBlob

#Define some example patterns and responses
patterns_responses = {
    "hi":"Hello! How can I assist you?",
    "how are you":"Hello, I'm here to help!",
    "bye":"Goodbye! Have a great day!"
}

def chatbot_response(user_input):
    #Create a TextBlob object for user input
    blob = TextBlob(user_input.lower())
    
    #Check for patterns in user input
    for pattern, response in patterns_responses.items():
        if pattern in blob.words:
            return response
    #If no pattern matches, provide a default response
    return "I'm sorry, I don't understand. Can you rephrase?" 

#Chatbot loop
print("Chatbot: Hello! How can I assist you? (Type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)

