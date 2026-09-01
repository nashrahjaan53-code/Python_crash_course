from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Hello! Explain Python in simple words."
)

print(response.output_text)
