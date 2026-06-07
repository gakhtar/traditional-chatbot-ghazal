"""
Traditional Rule-Based Chatbot
Author: Ghazal Akhtar
Description:
This chatbot uses simple rule-based logic instead of an LLM.
It responds to greetings, help requests, project questions,
and malformed input.
"""

import re


def normalize_text(user_input):
    """
    Convert input to lowercase and remove extra spaces.
    """
    return user_input.lower().strip()


def get_bot_response(user_input):
    """
    Return chatbot response based on rule-based pattern matching.
    """

    text = normalize_text(user_input)

    if text == "":
        return "I did not receive any input. Please type a question or type 'help'."

    if re.search(r"\b(hi|hello|hey)\b", text):
        return "Hello! I am a simple traditional chatbot. Type 'help' to see what I can do."

    elif "help" in text or "capabilities" in text or "what can you do" in text:
        return (
            "I can do the following:\n"
            "1. Greet you\n"
            "2. Explain what a chatbot is\n"
            "3. Describe the chatbot development lifecycle\n"
            "4. Tell you about this project\n"
            "5. Handle unknown or malformed input"
        )

    elif "what is a chatbot" in text or "define chatbot" in text:
        return (
            "A chatbot is a software application that simulates conversation "
            "with users. This chatbot uses traditional rule-based logic instead "
            "of artificial intelligence or a large language model."
        )

    elif "lifecycle" in text or "development lifecycle" in text:
        return (
            "The chatbot development lifecycle includes planning, designing, "
            "building, testing, deployment, and maintenance. In this project, "
            "I planned the bot's purpose, created rules, tested responses, "
            "and prepared the code for GitHub submission."
        )

    elif "project" in text or "assignment" in text:
        return (
            "This project demonstrates a simple traditional chatbot. It uses "
            "if-else rules and keyword matching to generate responses."
        )

    elif "bye" in text or "goodbye" in text or "exit" in text or "quit" in text:
        return "Goodbye! Thank you for testing the chatbot."

    elif len(text) < 3:
        return "That input is too short for me to understand. Please type a complete question."

    else:
        return (
            "I am sorry, I did not understand that. "
            "Please type 'help' to see the questions I can answer."
        )


def main():
    """
    Run chatbot in command line.
    """
    print("Traditional Chatbot")
    print("Type 'help' to see what I can do.")
    print("Type 'exit' or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)

        if normalize_text(user_input) in ["exit", "quit", "bye", "goodbye"]:
            break


if __name__ == "__main__":
    main()
