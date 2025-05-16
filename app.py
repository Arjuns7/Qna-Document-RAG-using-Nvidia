from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="google/gemma-2-27b-it",
  messages=[{"role":"user","content":"Provide me latest update about machine learning"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
