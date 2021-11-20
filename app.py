import openai

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
  engine="davinci",
  prompt="Q: "+str(input("Input:")),
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n\nQ:"]
)

# print(response)
print(response['choices'][0].text)