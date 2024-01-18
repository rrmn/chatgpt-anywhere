# ChatGPT Anywhwere
This is a tutorial and flask/bulma/mysql template to deploy a simple ChatGPT app on PythonAnywhere.com

![chatgpt-anywhere](https://github.com/rrmn/chatgpt-anywhere/assets/14080347/0a73b07e-099c-4369-a2d4-43a77aaa6984)


# Installation

## 0. Create an account on PythonAnywhere.com
1. Create an account on PythonAnywhere.com. It can be a free account for starters. If you want to support me you can use this affiliate [link to PythonAnywhere.com](https://www.pythonanywhere.com/?affiliate_id=00ffc226).
1. Remember your `username` (the user name which you use to login into PythonAnywhere.com). It will be important later.
1. Once you have created an account, create a web app through the interface. Remember your `webappname`.
1. Also check out the `CONSOLES` part of the dashboard. You will need to creat and use a `bash console` later.
1. Once you are comfortable with the interface, you can basically focus on these 3 important places:
    1. **Working directory**: pythonanywhere.com/user/{username}/files/home/{webappname}
    1. **Web App Admin Interface**: pythonanywhere.com/user/{username}/webapps/`
    1. **Bash console**: pythonanywhere.com/user/{username}/ --> CONSOLES

## 1. Setup Python

1. Copy all files into your **working directory** 
1. Open a **bash console**
1. Create a virtual environment so that everything regarding Python's versions is nice and separated:
    1. Run `venv python -m venv myvenv`
    1. Run `source myvenv/bin/active` 
    1. Your console should now have a `(myenv)` prefix
    1. To verify that it works, run `which python`. It should look something like this: `username/myvenv/bin/python` (the important part is `myvenv`)
1. Install necessary packages: `pip install -r requirements.txt`. Resolve all errors as they arise.

## 2. Setup OpenAI

### Account
1. Get an OpenAI paid account (something like 20$ / month)

### Assistant ID
1. Go to platform.openai.com
1. Create a new `Assistant` (You can leave most fields blank for starters. I recommend using `gpt-4` as the model, but it's up to you)
1. Next to the `Name` of your `Assistant` you will see an `ID` that looks something like this: `asst_AAAaaaaa12341234bbBBBbb`. Leave this window open.
1. In another window, go to a file called `.env` in your working directory. (If it doesn't exist: create a file with this name) 
1. OVERWRITE the value of the `OPENAI_ASSISTANT_ID` with your new ID, so it reads
    ```
    OPENAI_ASSISTANT_ID = "asst_AAAaaaaa12341234bbBBBbb"
    ```
    (or whatever your Assistant's ID is)

### API Keys
1. Go to platform.openai.com
1. Create a new set of `API Keys` 
1. Next to the `Name` of your `Assistant` you will see an `ID` that looks something like this: `sk-abc123abc123abc`. Leave this window open.
    1. ATTENTION: This will only be shown ONCE! If you fail to write this value down, you will need to create a new set of keys.
1. In another window, go back to your `.env` file. 
1. OVERWRITE the value of the `OPENAI_API_KEY` with your new key, so it reads
    ```
    OPENAI_API_KEY = "sk-abc123abc123abc"
    ```
    (or whatever your key is)

## 3. Done
1. Run flask (e.g. by pressing `Reload Webapp` on PythonAnywhere.com)
1. Go to  {username).pythonanywhere.com to see your web app running.
1. ???
1. Profit 🤩

This was a quick write-up. If you run into any errors or problems, feel free to open up an issue here on Github.



