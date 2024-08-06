import openai


openai.api_key = "Set your OpenAI API key"

def send_message(message_log):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log
    )
    return completion.choices[0].message['content']

# Main function that runs the chatbot
def main():
    # Initialize the conversation history with a message from the chatbot
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        message_log.append({"role": "user", "content": user_input})
        response = send_message(message_log)
        print(f"AI assistant: {response}")
        message_log.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()

