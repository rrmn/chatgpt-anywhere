from flask import Flask, render_template, request, jsonify, json
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
from flask import Flask
from datetime import datetime


# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Initialize OpenAI
client = OpenAI()

def answer_question(user_input):
    
    assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
    api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        # Assuming you have set OPENAI_API_KEY in your .env file
        client.api_key = api_key

        my_thread = client.beta.threads.create()
        print(f"This is the thread object: {my_thread} \n")

        # Step 3: Add a Message to a Thread
        my_thread_message = client.beta.threads.messages.create(
            thread_id = my_thread.id,
            role = "user",
            content=f"Answer the following question: {user_input})",
        )
        print(f"This is the message object: {my_thread_message} \n")

        # Step 4: Run the Assistant
        my_run = client.beta.threads.runs.create(
            thread_id = my_thread.id,
            assistant_id = assistant_id,
        )
        print(f"This is the run object: {my_run} \n")

        # Step 5: Periodically retrieve the Run to check on its status to see if it has moved to completed
        while my_run.status in ["queued", "in_progress"]:
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id, run_id=my_run.id
            )

            if keep_retrieving_run.status == "completed":
                print("\n")

                # Step 6: Retrieve the Messages added by the Assistant to the Thread
                all_messages = client.beta.threads.messages.list(thread_id = my_thread.id)

                user_message = my_thread_message.content[0].text.value
                assistant_message = all_messages.data[0].content[0].text.value

                print(f"# User:\n{user_message} \n")
                print(f"# Assistant:\n{assistant_message} \n")

                return assistant_message  # Return the content directly

            elif (
                keep_retrieving_run.status == "queued"
                or keep_retrieving_run.status == "in_progress"
            ):
                dt = datetime.now()
                print(f"Run status: {keep_retrieving_run.status}", dt)
                time.sleep(3)
                pass

            else:
                print(f"Run status: {keep_retrieving_run.status}")
                break

        return (
            my_run["data"]["text"]
            if "data" in my_run and "text" in my_run["data"]
            else "No response"
        )
    except Exception as e:
        return str(e)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/ask-chatgpt", methods = ["POST"])
def ask_chatgpt():
    data = request.json
    question = data.get("user_input")
    print(
        f"User asked: {question} \n"
    )
    response = answer_question(question)

    return response

