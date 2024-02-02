# ChatGPT Anywhere: Beginner's Guide
This is a beginner's guide for deploying a simple ChatGPT application using Flask and Bulma on PythonAnywhere.com. This tutorial will help you set up your own ChatGPT app, even if you're new to programming or web development.

![chatgpt-anywhere](https://github.com/rrmn/chatgpt-anywhere/assets/14080347/0a73b07e-099c-4369-a2d4-43a77aaa6984)

## Getting Started

### Step 1: Sign Up on PythonAnywhere
1. **Create a PythonAnywhere Account**: Visit PythonAnywhere.com  and sign up. (You can use this [affiliate link](https://www.pythonanywhere.com/?affiliate_id=00ffc226) if you want to support me). You can start with a free account. 
2. **Note Your Username**: Remember your username. You'll need it for setting up your web app.
3. **Create a Web App**: Once logged in, use the dashboard to create a new web app. Note down your `webappname`.
4. **Familiarize with the Dashboard**: Explore the **Consoles** section. You'll use a `bash console` here.
5. **Key Areas to Focus**: 
    - **Working Directory**: `pythonanywhere.com/user/{username}/files/home/{webappname}`
    - **Web App Admin Interface**: `pythonanywhere.com/user/{username}/webapps/`
    - **Bash Console**: Accessible from `pythonanywhere.com/user/{username}/` under **Consoles**.

### Step 2: Set Up Python
1. **Move Files to Working Directory**: Transfer all necessary files into your working directory.
2. **Launch a Bash Console**: From the dashboard, open a bash console.
3. **Create a Virtual Environment**:
    - Execute `python -m venv myvenv` to create a virtual environment.
    - Activate it with `source myvenv/bin/activate`. Your console should now show `(myvenv)` prefix.
    - Check with `which python`. It should display something like `.../myvenv/bin/python`.
4. **Install Dependencies**: Run `pip install -r requirements.txt` and resolve any installation errors. This usually takes some effort, but most things can be resolved with Googling.

### Step 3: Set Up OpenAI

#### Creating an OpenAI Account
1. **Register for OpenAI**: Sign up for a paid account on OpenAI (around $20/month).

#### Setting Up Assistant ID
1. **Create an Assistant on OpenAI**: Visit [OpenAI's platform](https://platform.openai.com), and create a new Assistant. You can use `gpt-4` as the model.
2. **Note the Assistant ID**: Find the `ID` next to your Assistant’s name, like `asst_AAA...`. Keep this window open.
3. **Configure `.env` File**:
    - In your working directory, find or create a `.env` file.
    - Replace the `OPENAI_ASSISTANT_ID` value with your Assistant's ID.

#### Generating API Keys
1. **Create API Keys on OpenAI**: Still on [OpenAI's platform](https://platform.openai.com), generate a new set of API keys.
2. **Secure Your API Key**: Note the key, which looks like `sk-abc123...`. It's shown only once!
3. **Update `.env` File**:
    - Return to the `.env` file.
    - Update `OPENAI_API_KEY` with your new API key.

### Step 4: Launch Your App
1. **Start Flask**: Use PythonAnywhere's interface to run Flask, usually with `Reload Webapp`.
2. **Access Your Web App**: Visit `{username}.pythonanywhere.com` to see your app in action.
3. **Enjoy Your Creation**: Experiment and explore your new ChatGPT app!
4. **Celebrate 🎉**: You've successfully deployed a ChatGPT app!

For any issues or questions, feel free to open an issue on this Github repository.
