import streamlit as st
from openai import OpenAI
from functions import *
import os
import random
import time

logo = "icons/ramlogo.png"

st.set_page_config(
    page_title="Daily Questions",
    page_icon=logo,
    layout="wide",
)

st.title(':blue[Welcome to daily questions for Ramboll Tech!]')

#Change to True to use the system variable OPENAI_API_KEY
client = initialize_openai_client(use_env_variable=True)

selected_model = "gpt-4o"  
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = selected_model


def daily_question(model, client):
    message = display_random_message()

    with st.spinner(message):
        time.sleep(2)  # Dramatic pause

        command = (
            send_random_prompt()
        )
        return question_answer(message=command, model=model, client=client)


def input_participants():
    num_input = st.text_input("Number of raised hands") #fuck off
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

    if participant_count > 0:

        question = daily_question(model=selected_model, client=client)

        selected = random.randint(1, participant_count)
        st.write(f"Question for participant number {selected}: \n\n", question)
    else:
        st.warning("Please enter a number greater than 0")
    

