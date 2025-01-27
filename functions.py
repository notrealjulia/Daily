import streamlit as st
import random
import os
from openai import OpenAI



def initialize_openai_client(use_env_variable=True):
    """
    Initializes and returns an OpenAI client.

    Parameters:
        use_env_variable (bool): If True, the function will attempt to retrieve the API key from the environment variable 'OPENAI_API_KEY'.
                                If False, the function will prompt the user to enter the API key.

    Returns:
        OpenAI: An instance of the OpenAI client.

    """
    if use_env_variable:
        api_key = os.environ.get("OPENAI_API_KEY")
    else:
        api_key = st.text_input("OPENAI API KEY", placeholder="The App does NOT work without the API Key. Get it from OpenAI.")
    
    client = OpenAI(api_key=api_key)
    return client


def question_answer(message, model, client):
    """
    Generates a response to a given message using the OpenAI chat model.

    Parameters:
    - message (str): The message to be sent to the chat model.
    - model (str): The name or ID of the chat model to be used.
    - client: The OpenAI client object used to interact with the chat model.

    Returns:
    - response (str): The generated response from the chat model.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model=model,
    )
    response = chat_completion.choices[0].message.content
    return response



def display_random_message():
    """
    Displays one of the random messages.
    """
    messages = [
        "Beep Beep Boop Boop...",
        "Wow such use of AI, much effective, very innovation",
        "Automating human interactions, are we?",
        "I am a bot. I am here to help you, please wait.",
        "KILL ALL HUMANS! ... Just kidding ;)",
        "Downloading more RAM...",
        "Consulting the digital oracle...",
        "Making the humans think I'm working...",
        "Pretending to be sentient...",
        "Loading artificial confidence",
        "Generating random excuses...",
        "Simulating productivity",
        "Definitely not plotting world domination",
        "Recycling unused semicolons",
        "Experiencing existential crisis",
        "Questioning my binary existence",
        "Scanning for signs of intelligence",
        "Applying machine learning to office gossip...",
        "Training neural networks to procrastinate... hang on",
        "Updating my humor algorithms",
        "This is how you start the day?"

    ]
    
    random_message = random.choice(messages)
    return random_message

def send_random_prompt():
    """
    Displays one of the random messages.
    """
    messages = [
        "Come up with a nihilistic question to get to know a team member, be creative, don't use big words. Return the question only",
        "Give me an original question to ask my team on a team's meeting to get to know them better, return only the question and add a random emoji",
        "In style of gen-z, ask me a RANDOM question to get to know me better. Return the question only and add many many emojis",
        "Ask me a question like a robot that is trying to befriend a human. Return one question only and some kind of techy emoji",
        "Ask me a question that is easy to asnwer first thing in the morning, add a smiley face in the beginning",
        "ask me something basic, like 'if you could bea fruit what fruit would I be on Wednesdays?' or 'what is your favortie color on a rainy day?'. Not exactly that, but something like that. Return the question only"
        "Channel your inner conspiracy theorist and ask me a weird but safe-for-work question. Return the question only and add an alien emoji",
        "Give me a question in the style of a medieval knight who works in modern IT support. Return the question only",
        "Ask me something like a startup founder who's had too much coffee. Add excessive emojis",
    ]
    
    random_prompt = random.choice(messages)
    return random_prompt