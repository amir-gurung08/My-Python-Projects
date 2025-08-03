from openai import OpenAI,RateLimitError

client = OpenAI(
  api_key="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"
)

try:
    response = client.responses.create(
    model="gpt-4o-mini",
    input="write a haiku about ai",
    store=True,
    )

    print(response.output_text);

except RateLimitError as e:
    print("Quota exceeded. Please check your OpenAI account limits.")
