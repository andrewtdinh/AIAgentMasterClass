import asana
import asana.configuration
from asana.rest import ApiException
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
import os

load_dotenv()

client = OpenAI()
model = os.getenv('OPENAI_MODEL', 'gpt-4o')

configuration = asana.Configuration()
configuration.access_token = os.getenv('ASANA_ACCESS_TOKEN', '')
api_client = asana.ApiClient(configuration)

task_api_instance = asana.TasksApi(api_client)

def main():
  messages = [
    {
      "role": "system",
      "content": f"You are a personal assistant who helps manage tasks in Asana. The current date is: {datetime.now().date()}"
    }
  ]

  while True:
    user_input = input("Chat with AI (q to quit): ").strip()

    if user_input == 'q':
      break

    messages.append({"role": "user", "content": user_input})
    ai_response = prompt_ai(messages)

    print(ai_response)
    messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
  main()