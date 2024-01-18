# ChatGPT Anywhwere
This is a tutorial and flask/bulma/mysql template to deploy a simple ChatGPT app on PythonAnywhere.com

# Installation
## 1. Setup Python
1. Copy all files into your working directory 
1. Open a bash console
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
1. Create a new `Assistant` (you can leave most fields blank, but I recommend using `ChatGPT-4`` as the model)
1. Next to the `Name` of your `Assistant`` you will see an `ID` that looks something like this: `asst_AAAaaaaa12341234bbBBBbb`. Leave this window open.
1. In another window, go to a file called `.env` in your working directory. (If it doesn't exist: create a file with this name) 
1. OVERWRITE the value of the `OPENAI_ASSISTANT_ID` with your new ID, so it reads `OPENAI_ASSISTANT_ID = "asst_AAAaaaaa12341234bbBBBbb"` (or whatever your Assistant's ID is)
### API Keys
1. Go to platform.openai.com
1. Create a new set of `API Keys` 
1. Next to the `Name` of your `Assistant`` you will see an `ID` that looks something like this: `sk-abc123abc123abc`. Leave this window open.
    1. ATTENTION: This will only be shown ONCE! If you fail to write this value down, you will need to create a new set of keys.
1. In another window, go back to your `.env` file. 
1. OVERWRITE the value of the `OPENAI_API_KEY` with your new key, so it reads `OPENAI_API_KEY = "sk-abc123abc123abc"` (or whatever your key is)
## 3. Done
1. Run flask (e.g. by pressing `Reload Webapp` on PythonAnywhere.com)
1. Profit 🤩

This was a quick write-up. If you run into any errors or problems, feel free to open up an issue here on Github.



