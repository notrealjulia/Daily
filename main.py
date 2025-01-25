import streamlit as st
from openai import OpenAI
import os
import random
import time

logo = "icons/ramlogo.png"


st.set_page_config(
    page_title="Daily Questions",
    page_icon=logo,
    layout="wide"
)


selected_model = "gpt-4o"  # Setting the default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = selected_model



st.title(':blue[Welcome to daily questions for Ramboll Tech!]')


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
        "KILL ALL HUMANS! ... Just kidding ;)"
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
        "Come up with a nihilistic question to get to know a team member better, be creative, don't use big words",
        "Give me an original question to ask my team in the daily standup add a food emoji",
        "Make a question that asks my collegue to get to know them better, keep it short and in style of gen-z, add too many emojis",
        "Ask me something personal, but not too personal, something that would make me think. Return only the question",
        "Ask 1 question like a robot that is trying to befriend a human, and some kind of robot emoji"
        "Ask me obscure question, something that a creative person like Bjork could ask, make it personal to me. Return the question only."
        "Ask me a question that is easy to asnwer first thing in the morning, add a smiley face in the beginning",
    ]
    
    random_prompt = random.choice(messages)
    return random_prompt

def daily_question(model, client):
    message = display_random_message()

    with st.spinner(message):
        time.sleep(2)  # Dramatic pause

        command = (
            send_random_prompt()

        )

        return question_answer(message=command, model=model, client=client)

#Change to True to use the system variable OPENAI_API_KEY
client = initialize_openai_client(use_env_variable=True)


def input_participants():
    # Simple text input with large styling
    num_input = st.text_input(
        "Number of raised hands",
        #value="0",
        key="large_input"
    )
    
    # Convert input to integer if possible
    try:
        num_participants = int(num_input)
        if num_participants < 0:
            st.error("Please enter a positive number")
            return 0
        return num_participants
    except ValueError:
        if num_input != "":  # Only show error if input is not empty
            st.error("Please enter a valid number")
        return 0


participant_count = input_participants()

if st.button("Submit"):
        # Get the number of participants

    # Use the value wherever needed
    if participant_count > 0:

        question = daily_question(model=selected_model, client=client)

        selected = random.randint(1, participant_count)
        st.success(f"Selected participant number: {selected}")
        st.write("Question for you: \n\n", question)
    else:
        st.warning("Please enter a number greater than 0")
    

