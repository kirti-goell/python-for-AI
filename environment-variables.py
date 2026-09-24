# Environment variable is a key - value pair stored outside your programs source code that provides configuration or
# sensitive info to your application while it is running

# ex: API_KEY = "abc123xyz"

# purposes:
# 1. keep sensitive info out of your code, you dont want them to pushed accidentally to github
# 2. make the same code work in diff envs

# environment variable is not equals to .env file remember

#  we can export the api_key in the terminal then we will get the value of api key but if we open 
# up the new terminal then its not vailable there

#  to avoid this we have another method i.e. using .env files
# .env files := the easiest way to manage secrets
# it is a simple text file that stores environment variables. Instead of typing export command , you directly write once in the file

# 1. create .env file (remeber i have already excluded it from the gitignore)

# 2. lets see how we will get the values and run pip install python-dotenv
import os
from dotenv import load_dotenv

# to load the .env file
load_dotenv()

# read from environments
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')

print(f"using api key: {api_key}")
